# Modelo Pedagógico Social-Cognitivo-Sistémico · CECAR

Recurso educativo digital de lectura interactiva para el Diplomado en Docencia Universitaria. El contenido es una síntesis pedagógica del documento de `docs/Modelo Pedagógico.docx` (pp. 38–45).

## Publicación

El sitio es estático: `index.html`, `styles.css`, `script.js`, `assets/` y `modelo-pedagogico-cecar.pdf`. No requiere compilación, servidor de aplicaciones ni token. Puede publicarse directamente desde la raíz del repositorio en GitHub Pages o en Cloudflare Pages con **build command** vacío y **output directory** `.`. El archivo `.env` está excluido por `.gitignore`; si se suben archivos manualmente, no se debe incluir.

Para previsualizarlo localmente:

```bash
python -m http.server 4173
```

Abrir `http://localhost:4173`.

## PDF

El archivo descargable ya está incluido. Para regenerarlo después de modificar su contenido:

```bash
python -m pip install reportlab
python tools/build_pdf.py
```

La experiencia interactiva funciona en el navegador sin formularios que almacenen respuestas; la pregunta de comprobación da retroalimentación inmediata. El PDF reúne la lectura y la situación de aplicación en formato de consulta.
