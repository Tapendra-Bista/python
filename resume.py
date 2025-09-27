from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import inch

# Create PDF
pdf = SimpleDocTemplate(
    "premjeet_flutter_resume.pdf",
    pagesize=letter,
    leftMargin=0.75 * inch,
    rightMargin=0.75 * inch,
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch,
)

# Get default styles
styles = getSampleStyleSheet()

# Modify existing styles instead of adding duplicates
styles['Title'].fontSize = 18
styles['Title'].alignment = TA_CENTER
styles['Title'].spaceAfter = 6

# Check if style exists before adding
if 'Subtitle' not in styles:
    styles.add(ParagraphStyle(name="Subtitle", fontSize=12, alignment=TA_CENTER, textColor=colors.grey))
if 'SectionHeader' not in styles:
    styles.add(ParagraphStyle(name="SectionHeader", fontSize=14, spaceBefore=12, spaceAfter=6))
if 'Body' not in styles:
    styles.add(ParagraphStyle(name="Body", fontSize=10, spaceAfter=6))
if 'Bullet' not in styles:
    styles.add(ParagraphStyle(name="Bullet", fontSize=10, leftIndent=10, bulletIndent=5, spaceAfter=6))
else:
    # Modify existing Bullet style if it exists
    styles['Bullet'].leftIndent = 10
    styles['Bullet'].bulletIndent = 5
    styles['Bullet'].spaceAfter = 6

# Content
content = []

# Header
content.append(Paragraph("Premjeet Sahu", styles["Title"]))
content.append(Paragraph("Flutter Developer | +91-9575768300 | premjeet.career@gmail.com", styles["Subtitle"]))
content.append(Paragraph("LinkedIn: <link href='https://linkedin.com/in/Premjeet'>linkedin.com/in/Premjeet</link> | GitHub: <link href='https://github.com/Premjeet'>github.com/Premjeet</link>", styles["Body"]))

# Experience (Edited for Flutter)
content.append(Paragraph("Experience", styles["SectionHeader"]))

exp_data = [
    [Paragraph("<b>Infosys - Flutter Developer</b>", styles["Body"]), 
     Paragraph("Pune, Maharashtra | Feb 2025 – Present", styles["Body"])],
    [
        Paragraph("• Developed cross-platform mobile apps using Flutter, improving performance by 25%.", styles["Bullet"]),
        Paragraph("• Integrated Firebase for authentication and real-time database operations.", styles["Bullet"]),
        Paragraph("• Collaborated with designers to implement responsive UIs with Figma.", styles["Bullet"]),
    ],
    [Paragraph("<b>Infosys - Trainee</b>", styles["Body"]), 
     Paragraph("Mysore, Karnataka | Sep 2024 – Jan 2025", styles["Body"])],
    [
        Paragraph("• Built 3+ Flutter apps with REST API integration (Dio, Retrofit).", styles["Bullet"]),
        Paragraph("• Used Git for version control and Agile for project management.", styles["Bullet"]),
    ],
]

exp_table = Table(exp_data, colWidths=[4 * inch, 2 * inch])
exp_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("BACKGROUND", (0, 2), (-1, 2), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("TEXTCOLOR", (0, 2), (-1, 2), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("SPAN", (0, 1), (-1, 1)),
            ("SPAN", (0, 3), (-1, 3)),
        ]
    )
)
content.append(exp_table)

# Projects (Flutter Focus)
content.append(Paragraph("Projects", styles["SectionHeader"]))

projects = [
    [Paragraph("<b>Expense Tracker App</b>", styles["Body"]), 
     Paragraph("Flutter, Firebase | Jan 2025", styles["Body"])],
    [
        Paragraph("• A budget management app with real-time sync using Firestore.", styles["Bullet"]),
        Paragraph("• Implemented BLoC state management for scalable architecture.", styles["Bullet"]),
    ],
    [Paragraph("<b>Travel Journal App</b>", styles["Body"]), 
     Paragraph("Flutter, Google Maps API | Nov 2024", styles["Body"])],
    [
        Paragraph("• Interactive map to document travel adventures with photo uploads.", styles["Bullet"]),
        Paragraph("• Used Provider for state management and Hive for offline storage.", styles["Bullet"]),
    ],
]

# Add projects to content
for i in range(0, len(projects), 2):
    content.append(projects[i][0])
    content.append(projects[i][1])
    for bullet in projects[i + 1]:
        content.append(bullet)

# Skills
skills = "Languages: Dart, Java, JavaScript\nFrameworks: Flutter, Firebase, Node.js\nTools: Android Studio, VS Code, Git, Figma"
content.append(Paragraph("Technical Skills", styles["SectionHeader"]))
content.append(Paragraph(skills, styles["Body"]))

# Build PDF
pdf.build(content)
print("PDF generated successfully: premjeet_flutter_resume.pdf")