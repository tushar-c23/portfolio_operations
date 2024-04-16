from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()

def drop_rows_with_empty_array(df):
    for index, row in df.iterrows():
        if not row['top_10'] or row['top_10'] == '[]':
            df.drop(index, inplace=True)

total_portfolio_vals = {}
total_slot_vals = []

@app.post("/uploadfile/")
async def upload_file(csv_file: UploadFile = File(...)):
    df = pd.read_csv(csv_file.file)
    drop_rows_with_empty_array(df)
    
    prev_values = [100,100,100,100,100,100,100,100,100,100]
    
    for index, row in df.iterrows():
        percent_changes = [float(x) for x in row['percent_change_values'][1:-1].split(',') if x.strip()]
        curr_values = []
        for i in range(len(prev_values)):
            curr_values.append(prev_values[i] * (1 + percent_changes[i] / 100))
        total_portfolio_vals[row['datetime']] = sum(curr_values)
        prev_values = curr_values
        total_slot_vals = curr_values
    
    print("Final values of the slots: ",total_slot_vals)
    print("Final postfolio value: ",(sum(total_slot_vals)))
    
    keys = list(total_portfolio_vals.keys())
    values = list(total_portfolio_vals.values())
    plt.plot(keys, values, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Portfolio Value over time')
    plt.grid(True)
    keys_to_display = list(total_portfolio_vals.keys())[::100]
    plt.xticks(keys_to_display,rotation=45)
    plt.gcf().set_size_inches(18, 9) 
    plt.savefig('plot.png')
    plt.show()

    
    return {"filename": csv_file.filename,
            "Final values of the slots": total_slot_vals,
            "Final postfolio value": (sum(total_slot_vals))}