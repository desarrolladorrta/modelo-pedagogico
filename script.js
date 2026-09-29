const nodeContent = {
  docencia: { number: '01 / 03', title: 'Docencia', text: 'Contextualiza el conocimiento mediante procesos pedagógicos y didácticos que parten del análisis y la reflexión de situaciones reales.' },
  investigacion: { number: '02 / 03', title: 'Investigación', text: 'Indaga y explora los problemas del contexto para construir conocimiento científico y tecnológico desde las preguntas que surgen de la realidad.' },
  extension: { number: '03 / 03', title: 'Extensión', text: 'Transfiere los saberes construidos a los escenarios donde actúan las personas y contribuye a su transformación.' }
};

document.querySelectorAll('.system-node').forEach(button => {
  button.addEventListener('click', () => {
    const item = nodeContent[button.dataset.node];
    document.querySelectorAll('.system-node').forEach(node => { node.classList.toggle('selected', node === button); node.setAttribute('aria-pressed', String(node === button)); });
    document.getElementById('nodeNumber').textContent = item.number;
    document.getElementById('nodeTitle').textContent = item.title;
    document.getElementById('nodeText').textContent = item.text;
  });
});

document.querySelectorAll('.accordion-item button').forEach(button => {
  button.addEventListener('click', () => {
    const item = button.closest('.accordion-item');
    const willOpen = !item.classList.contains('open');
    document.querySelectorAll('.accordion-item').forEach(other => {
      other.classList.remove('open');
      other.querySelector('button').setAttribute('aria-expanded', 'false');
      other.querySelector('.accordion-panel').hidden = true;
    });
    if (willOpen) { item.classList.add('open'); button.setAttribute('aria-expanded', 'true'); item.querySelector('.accordion-panel').hidden = false; }
  });
});

const quiz = document.getElementById('quiz');
quiz.querySelectorAll('button').forEach(button => {
  button.addEventListener('click', () => {
    const correct = button.dataset.correct === 'true';
    quiz.querySelectorAll('button').forEach(option => { option.classList.remove('chosen', 'correct'); option.setAttribute('aria-pressed', String(option === button)); });
    button.classList.add('chosen');
    if (correct) button.classList.add('correct');
    const feedback = document.getElementById('quizFeedback');
    feedback.hidden = false;
    feedback.className = `quiz-feedback ${correct ? 'success' : 'retry'}`;
    feedback.innerHTML = correct ? '<strong>Exactamente.</strong> La propuesta conecta contexto, investigación, diálogo de saberes y transformación social.' : '<strong>Vuelve a pensar la relación.</strong> El modelo integra los saberes con los problemas reales y promueve participación activa. Puedes elegir otra respuesta.';
  });
});

const sections = [...document.querySelectorAll('.sheet[id]')];
const links = [...document.querySelectorAll('.contents a')];
const progress = document.getElementById('readingProgress');
const percentage = document.getElementById('readingPercent');
let ticking = false;
function updateReading() {
  const total = document.documentElement.scrollHeight - window.innerHeight;
  const amount = total > 0 ? Math.min(100, Math.max(0, Math.round(window.scrollY / total * 100))) : 100;
  progress.style.width = `${amount}%`;
  percentage.textContent = `${amount} % leído`;
  const active = [...sections].reverse().find(section => section.getBoundingClientRect().top <= window.innerHeight * .35) || sections[0];
  links.forEach(link => { const current = link.getAttribute('href') === `#${active.id}`; link.classList.toggle('active', current); if (current) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
  ticking = false;
}
window.addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(updateReading); ticking = true; } }, { passive: true });
window.addEventListener('resize', updateReading);
updateReading();

const sidebar = document.getElementById('sidebar');
const indexButton = document.getElementById('mobileIndex');
const scrim = document.getElementById('sidebarScrim');
function setMenu(open) { sidebar.classList.toggle('open', open); indexButton.setAttribute('aria-expanded', String(open)); indexButton.setAttribute('aria-label', open ? 'Cerrar índice' : 'Abrir índice'); scrim.hidden = !open; document.body.classList.toggle('menu-open', open); }
indexButton.addEventListener('click', () => setMenu(!sidebar.classList.contains('open')));
scrim.addEventListener('click', () => setMenu(false));
links.forEach(link => link.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', event => { if (event.key === 'Escape' && sidebar.classList.contains('open')) { setMenu(false); indexButton.focus(); } });
