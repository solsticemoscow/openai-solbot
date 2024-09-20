from fastapi import FastAPI, Request, HTTPException, status, Depends
from starlette.responses import RedirectResponse, HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from BOT.config import ROOT_DIR

app = FastAPI()

templates = Jinja2Templates(directory="HTML")


@app.get("/test2")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})


@app.get("/t", response_class=HTMLResponse)
async def read_html_page():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Select Time</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            background: linear-gradient(135deg, rgba(0, 0, 0, 0.2), rgba(255, 255, 255, 0.5)), url('https://source.unsplash.com/random/1600x900') no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
            color: #333;
        }
        .container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        h2 {
            font-family: 'Courier New', Courier, monospace;
            color: #333;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 class="font-monospace">Select Time</h2>
        <form id="timeForm">
            <div class="mb-3">
                <label for="hours" class="form-label">Hour</label>
                <select class="form-select" id="hours" required>
                    <option value="" disabled selected>Select hour</option>
                    <option value="00">00</option>
                    <option value="01">01</option>
                    <option value="02">02</option>
                    <option value="03">03</option>
                    <option value="04">04</option>
                    <option value="05">05</option>
                    <option value="06">06</option>
                    <option value="07">07</option>
                    <option value="08">08</option>
                    <option value="09">09</option>
                    <option value="10">10</option>
                    <option value="11">11</option>
                    <option value="12">12</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="minutes" class="form-label">Minute</label>
                <select class="form-select" id="minutes" required>
                    <option value="" disabled selected>Select minute</option>
                    <option value="00">00</option>
                    <option value="15">15</option>
                    <option value="30">30</option>
                    <option value="45">45</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary w-100">Submit</button>
        </form>
    </div>
    <script>
        document.getElementById('timeForm').addEventListener('submit', function(event) {
            event.preventDefault();

            var hours = document.getElementById('hours').value;
            var minutes = document.getElementById('minutes').value;
            var time = {
                "hours": hours,
                "minutes": minutes
            };

            // Send data to the bot
            Telegram.WebApp.sendData(JSON.stringify(time));

            // Close the Web App
            Telegram.WebApp.close();
        });
    </script>
</body>
</html>




    """
    return html_content


@app.get(path="/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=9999)
