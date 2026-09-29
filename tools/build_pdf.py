"""Genera la versión de lectura descargable. Requiere: pip install reportlab."""
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "modelo-pedagogico-cecar.pdf"
FONT_DIR = Path("C:/Windows/Fonts")
if (FONT_DIR / "arial.ttf").exists():
    pdfmetrics.registerFont(TTFont("Body", str(FONT_DIR / "arial.ttf")))
    pdfmetrics.registerFont(TTFont("BodyBold", str(FONT_DIR / "arialbd.ttf")))
    pdfmetrics.registerFont(TTFont("Display", str(FONT_DIR / "georgia.ttf")))
else:
    # En entornos sin fuentes de Windows, las fuentes incluidas en ReportLab.
    FONT_DIR = Path(__import__("reportlab").__file__).parent / "fonts"
    pdfmetrics.registerFont(TTFont("Body", str(FONT_DIR / "Vera.ttf")))
    pdfmetrics.registerFont(TTFont("BodyBold", str(FONT_DIR / "VeraBd.ttf")))
    pdfmetrics.registerFont(TTFont("Display", str(FONT_DIR / "Vera.ttf")))

TEAL = colors.HexColor("#123d40")
GREEN = colors.HexColor("#a9c982")
INK = colors.HexColor("#19383a")
MUTED = colors.HexColor("#65756f")
RULE = colors.HexColor("#d9e2d9")

styles = {
    "title": ParagraphStyle("TitleCustom", fontName="Display", fontSize=27, leading=35, textColor=TEAL, spaceAfter=18),
    "lead": ParagraphStyle("LeadCustom", fontName="Body", fontSize=12, leading=19, textColor=TEAL, spaceAfter=19),
    "body": ParagraphStyle("BodyCustom", fontName="Body", fontSize=10.5, leading=17.5, textColor=INK, spaceAfter=13, alignment=TA_LEFT),
    "sub": ParagraphStyle("SubCustom", fontName="BodyBold", fontSize=11, leading=16, textColor=TEAL, spaceBefore=14, spaceAfter=6),
    "small": ParagraphStyle("SmallCustom", fontName="Body", fontSize=9, leading=14, textColor=MUTED, spaceBefore=12),
    "item": ParagraphStyle("ItemCustom", fontName="Body", fontSize=10.5, leading=17.5, textColor=INK, leftIndent=17, firstLineIndent=-12, spaceAfter=12),
}

sections = [
    ("Una mirada integradora", "El modelo Social-Cognitivo-Sistémico evoluciona la apuesta social-cognitiva de CECAR para responder a una realidad cambiante, diversa e interconectada.", [
        ("p", "Parte de la lectura del contexto institucional, local, nacional y global. Reconoce que las creencias, costumbres, tradiciones y condiciones sociales, económicas y culturales influyen en cómo las personas construyen conocimiento."),
        ("sub", "Aprender en relación"),
        ("p", "El modelo articula los componentes de la vida institucional para estudiar fenómenos y problemas de la realidad social. Docencia, investigación y extensión generan sinergias epistemológicas, teóricas y metodológicas, en lugar de operar como tareas aisladas."),
        ("p", "Esta perspectiva integradora e interdisciplinaria responde a los desafíos de la ciencia, la tecnología y la comunicación. El aprendizaje se evidencia en la construcción de conocimientos y saberes y en los resultados alcanzados durante la formación."),
        ("sub", "Idea central"),
        ("p", "Una institución es un conjunto de unidades interdependientes: las relaciones entre sus componentes permiten comprender el contexto y actuar sobre él."),
    ]),
    ("El conocimiento se construye en relación", "El modelo dialoga con distintas perspectivas para explicar cómo se aprende y por qué es necesario superar las miradas fragmentadas.", [
        ("sub", "Estructuralismo y teoría de sistemas"),
        ("p", "El estructuralismo estudia las relaciones entre los elementos de un fenómeno. La perspectiva sistémica reconoce la interdependencia de esos componentes y su articulación. La unidad y las conexiones ayudan a comprender problemas complejos y sustentan el trabajo interdisciplinario."),
        ("sub", "Pragmatismo y contexto"),
        ("p", "Los procesos pedagógicos parten del conocimiento del contexto geosociopolítico en que se desenvuelven los sujetos. Creencias, costumbres y tradiciones participan en la construcción de identidad y en las estructuras cognitivas. La interacción social favorece nuevas habilidades para aprender."),
        ("sub", "Perspectiva sociocrítica y cognitiva"),
        ("p", "La reflexión crítica sobre necesidades y problemas reales impulsa su transformación. La apropiación significativa del aprendizaje, el pensamiento crítico y la transferencia del saber se desarrollan en diálogo con otros y con el entorno."),
        ("small", "Referentes abordados en el texto fuente: Lévi-Strauss, Fals Borda, William James, Bertalanffy, Freire, Vygotsky, Ausubel, Bruner, Morin y Tamayo y Tamayo."),
    ]),
    ("Tres funciones, un mismo propósito", "La interdisciplinariedad conecta docencia, investigación y extensión en torno a problemas y posibilidades del contexto.", [
        ("sub", "Docencia"),
        ("p", "Contextualiza el conocimiento mediante procesos pedagógicos y didácticos que parten del análisis y la reflexión de situaciones reales."),
        ("sub", "Investigación"),
        ("p", "Indaga y explora los problemas del entorno para construir conocimiento científico y tecnológico a partir de preguntas que emergen de la realidad."),
        ("sub", "Extensión"),
        ("p", "Transfiere los saberes construidos a los escenarios donde se movilizan los actores y contribuye a su transformación."),
        ("p", "La relación entre estas funciones promueve el diálogo de saberes y una narrativa integradora: las preguntas del contexto alimentan la indagación, la construcción de conocimiento y su aplicación social."),
    ]),
    ("Principios que orientan la acción", "El modelo considera a la persona en todas sus dimensiones y entiende el contexto como un espacio de indagación, creación y transformación.", [
        ("sub", "Concepción antropológica"),
        ("p", "Comprende al ser humano en relación con las dimensiones culturales y sociales de su entorno, capaz de construir identidad, propósitos y vínculos con otros."),
        ("sub", "Constitución sistémica del saber pedagógico"),
        ("p", "Orienta una formación integral que articula dimensiones cognitivas, socioemocionales, afectivas, volitivas y físicas. Busca desarrollar capacidades, potencialidades, competencias y habilidades en ambientes que favorezcan la investigación y la innovación."),
        ("sub", "Investigación"),
        ("p", "Impulsa la indagación, exploración y búsqueda de los entramados del entorno. Comprender la realidad permite generar construcciones e innovaciones científicas, tecnológicas y técnicas."),
        ("sub", "Para pensar la práctica"),
        ("p", "¿Qué relaciones entre contexto, saberes y personas se hacen visibles en tu experiencia docente?"),
    ]),
    ("Un currículo en diálogo con la realidad", "Cinco principios conectan las decisiones curriculares con las necesidades de quienes aprenden y las transformaciones del entorno.", [
        ("sub", "1. Contextualización"),
        ("p", "Comprender la realidad de los actores, incluyendo globalización, ciencia, tecnología y objetivos de desarrollo sostenible, para abrir escenarios de innovación pedagógica, didáctica y curricular."),
        ("sub", "2. Aprendizaje"),
        ("p", "Apropiar conocimientos mediante procesos cognitivos y metacognitivos. Implica estimular el pensamiento crítico, creativo y divergente para aprender a pensar, a aprender y a desaprender."),
        ("sub", "3. Diálogo de saberes"),
        ("p", "Relacionar actores, perspectivas y escenarios. Considerar diferencias y antagonismos para comprender las dinámicas que conectan los saberes."),
        ("sub", "4. Procesos didácticos"),
        ("p", "Mediar la construcción significativa del conocimiento con estrategias dialogantes, análisis de situaciones reales y proyectos que favorezcan la investigación y la innovación."),
        ("sub", "5. Flexibilidad"),
        ("p", "Reconocer diferentes ritmos de aprendizaje, formas de trabajo, aspiraciones y miradas. Supone contextualizar y reconceptualizar de manera permanente la acción pedagógica."),
    ]),
    ("Formar para comprender y actuar", "La formación humana integra dimensiones socioemocionales, cognitivas, socioafectivas y físicas para afrontar los cambios del siglo XXI.", [
        ("p", "El modelo propone un currículo investigativo, interdisciplinario, flexible e integrado. Su horizonte es una persona con proyecto de vida personal y profesional, identidad caribe en diálogo con lo global, conciencia planetaria y compromiso con el desarrollo sostenible."),
        ("sub", "Del contexto a los resultados de aprendizaje"),
        ("item", "1. Reconocer las necesidades sociales y el contexto."),
        ("item", "2. Definir el propósito de formación y el perfil de egreso del programa."),
        ("item", "3. Formular los resultados de aprendizaje esperados."),
        ("item", "4. Articular la evaluación y la mejora continua."),
        ("p", "Cada programa académico declara un propósito de formación coherente con su identidad y sus apuestas misionales. De estas articulaciones surgen los resultados de aprendizaje y la estrategia de evaluación dentro del sistema de aseguramiento de la calidad."),
        ("sub", "La meta"),
        ("p", "Formar ciudadanos comprometidos con la transformación social de su región y del país mediante la apropiación de la ciencia y la tecnología, la investigación, el emprendimiento y la innovación."),
    ]),
    ("Evaluar es abrir un nuevo ciclo", "La evaluación es un proceso permanente y transparente de reflexión sobre capacidades, potencialidades y competencias; no se agota en emitir un juicio.", [
        ("p", "Requiere criterios explícitos, evidencias pertinentes y retroalimentación para tomar decisiones y mejorar. Los contenidos, las estrategias didácticas, las metodologías de evaluación y los resultados de aprendizaje deben estar articulados."),
        ("sub", "Un ciclo de mejora"),
        ("item", "Criterios claros → evidencias → reflexión → decisiones → mejora continua."),
        ("sub", "Una responsabilidad compartida"),
        ("p", "Para el docente, la evaluación permite revisar su práctica de aula y preguntarse qué enseña, por qué, para qué y cómo lo enseña. Para el estudiante, es una oportunidad de aprendizaje, monitoreo y autorregulación. La comunidad académica participa mediante autoevaluación, coevaluación y heteroevaluación."),
        ("p", "La evaluación también considera mediaciones pedagógicas, instrumentos, clima de aprendizaje y contextos socioculturales. La retroalimentación ayuda a deconstruir, construir y reconstruir la práctica educativa."),
    ]),
    ("Ideas para llevar al aula", "El modelo cobra vida cuando el contexto se convierte en pregunta, los saberes entran en diálogo y la evaluación ayuda a seguir aprendiendo.", [
        ("sub", "Una situación para considerar"),
        ("p", "Un grupo estudia un problema ambiental de su región. Una decisión coherente con el modelo sería indagar con el grupo el problema, integrar distintos saberes y proponer una respuesta con la comunidad. Así se articulan contexto, investigación, docencia, extensión y transformación social."),
        ("sub", "Tres preguntas para continuar"),
        ("item", "¿Qué problemas del contexto pueden convertirse en preguntas de aprendizaje?"),
        ("item", "¿Qué saberes y actores pueden entrar en diálogo para abordarlos?"),
        ("item", "¿Qué evidencias permitirían retroalimentar y mejorar el proceso?"),
        ("small", "Fuente: CECAR. Modelo Pedagógico: Social-Cognitivo desde la Perspectiva Sistémica, fragmento proporcionado para este recurso, pp. 38–45. Esta lectura reorganiza y sintetiza sus ideas con fines pedagógicos."),
    ]),
]


def decorate(canvas, doc):
    width, height = A4
    canvas.saveState()
    if doc.page == 1:
        canvas.setFillColor(TEAL)
        canvas.rect(0, 0, width, height, fill=1, stroke=0)
        logo = ROOT / "assets" / "logo-cecar.png"
        if logo.exists():
            canvas.drawImage(str(logo), 55, height - 98, width=139, height=43, mask="auto", preserveAspectRatio=True, anchor="sw")
        canvas.setStrokeColor(colors.HexColor("#7b9a86"))
        canvas.line(55, height - 133, width - 55, height - 133)
        canvas.setFillColor(colors.HexColor("#dceadd"))
        canvas.setFont("Body", 9)
        canvas.drawString(55, height - 161, "DIPLOMADO EN DOCENCIA UNIVERSITARIA")
        canvas.setFont("Display", 33)
        canvas.setFillColor(colors.white)
        canvas.drawString(55, height - 257, "Modelo Pedagógico")
        canvas.setFillColor(GREEN)
        canvas.setFont("Display", 23)
        canvas.drawString(55, height - 297, "Social-Cognitivo-Sistémico")
        canvas.setFont("Body", 12)
        canvas.setFillColor(colors.HexColor("#dfeade"))
        canvas.drawString(55, height - 353, "Una lectura para conectar teoría, práctica y contexto.")
        canvas.setStrokeColor(colors.HexColor("#779788"))
        canvas.line(55, 91, width - 55, 91)
        canvas.setFont("Body", 9)
        canvas.drawString(55, 67, "DOCENCIA · INVESTIGACIÓN · EXTENSIÓN")
        canvas.drawRightString(width - 55, 67, "CECAR")
    else:
        canvas.setFillColor(TEAL)
        canvas.rect(0, height - 15, width, 15, fill=1, stroke=0)
        canvas.setFont("BodyBold", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(55, height - 48, "CECAR  /  MODELO PEDAGÓGICO")
        canvas.setStrokeColor(RULE)
        canvas.line(55, height - 59, width - 55, height - 59)
        canvas.line(55, 56, width - 55, 56)
        canvas.setFont("Body", 8)
        canvas.drawString(55, 39, "Diplomado en Docencia Universitaria")
        canvas.drawRightString(width - 55, 39, f"{doc.page - 1:02d}")
    canvas.restoreState()


story = [Spacer(1, 500), PageBreak()]
for index, (title, lead, blocks) in enumerate(sections):
    story.extend([Paragraph(escape(title), styles["title"]), Paragraph(escape(lead), styles["lead"]), HRFlowable(width="100%", thickness=.7, color=RULE, spaceAfter=19)])
    for kind, text in blocks:
        story.append(Paragraph(escape(text), styles[kind if kind != "p" else "body"]))
    if index < len(sections) - 1:
        story.append(PageBreak())

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, topMargin=92, bottomMargin=75, leftMargin=55, rightMargin=55, title="Modelo Pedagógico Social-Cognitivo-Sistémico · CECAR", author="CECAR · Diplomado en Docencia Universitaria")
doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
print(f"PDF generado: {OUTPUT}")
