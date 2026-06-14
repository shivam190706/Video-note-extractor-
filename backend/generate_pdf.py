import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import cm
from datetime import datetime

def generate_pdf(notes, transcript):
    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/notes_{timestamp}.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title', parent=styles['Heading1'],
        fontSize=20, spaceAfter=20
    )
    heading_style = ParagraphStyle(
        'Heading', parent=styles['Heading2'],
        fontSize=14, spaceAfter=10
    )
    body_style = ParagraphStyle(
        'Body', parent=styles['Normal'],
        fontSize=11, spaceAfter=6, leading=16
    )
    timestamp_style = ParagraphStyle(
        'Timestamp', parent=styles['Normal'],
        fontSize=9, textColor='#7F77DD', spaceAfter=4
    )

    story = []

    # Title
    story.append(Paragraph("Video Notes", title_style))
    story.append(Paragraph(
        f"Generated on {datetime.now().strftime('%B %d, %Y at %H:%M')}",
        body_style
    ))
    story.append(Spacer(1, 0.5*cm))

    # Notes section
    story.append(Paragraph("AI Generated Notes", heading_style))
    for line in notes.split('\n'):
        if line.strip():
            story.append(Paragraph(line.strip(), body_style))
            story.append(Spacer(1, 0.2*cm))

    story.append(Spacer(1, 0.5*cm))

    # Transcript section
    story.append(Paragraph("Full Transcript", heading_style))
    for segment in transcript:
        start = round(segment['start'], 2)
        text = segment['text'].strip()
        story.append(Paragraph(f"[{start}s]", timestamp_style))
        story.append(Paragraph(text, body_style))

    doc.build(story)
    return filename