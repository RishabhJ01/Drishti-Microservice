from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from functions import generate_score_report, generate_pie_chart

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/hello")
async def hello():
    return {"message":"Welcome"}

@app.get("/hello/{name}")
async def hello_name(name):
    return {"message": f"Welcome {name}"}

@app.post("/generate_report")
async def generate_report(data: dict):
    # Extract data from JSON input
    graph_filename = await generate_score_report(data["scores"])
    pie_filename = await generate_pie_chart(data['satisfaction'])

    # Generate PDF report
    pdf_filename = "report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Add graph to the PDF
    story.append(Paragraph("Report", styles['Heading1']))
    story.append(Spacer(1, 12))
    img = Image(graph_filename)
    img.drawHeight = 400
    img.drawWidth = 600
    story.append(img)
    story.append(Spacer(1, 12))
    
    img2 = Image(pie_filename)
    img2.drawHeight = 400
    img2.drawHeight = 600
    story.append(img2)
    story.append(Spacer(1,12))

    # Build the PDF
    doc.build(story)

    return FileResponse(pdf_filename, media_type='application/pdf')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)