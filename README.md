## Steps to run:
1. Clone the repository
2. Install all requirements using `pip install -r requirements.txt`
3. Run the server ```uvicorn main:app --reload```
4. Your server will be live at your localhost:8000 or http://127.0.0.1:8000
5. Visit http://127.0.0.1:8000/docs to see the API documentation and try out the API
6. Upload the csv file and click on execute button
7. A plot will be generated and a png copy of the same will be saved in the current directory where you cloned the repository
8. The API response will include the following 2 things as a part of the JSON response:
    - The total portfolio value
    - The values of the slots of the portfolio