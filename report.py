import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_report(summary, insights):
    """
    Generate a PDF report.
    """

    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    filename = "reports/EDA_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Powered EDA Report</b>", styles["Title"]))

    story.append(Paragraph("<br/><b>Dataset Summary</b>", styles["Heading2"]))
    story.append(Paragraph(str(summary), styles["BodyText"]))

    story.append(Paragraph("<br/><b>Gemini AI Insights</b>", styles["Heading2"]))
    story.append(Paragraph(insights.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    return filename
