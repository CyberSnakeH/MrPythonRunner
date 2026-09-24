"""Editable TikZ sources, compiled by the application's bundled TikZJax worker."""

DIAGRAMS = {
    'couloir': r'''% Le couloir : une case par déplacement
\begin{tikzpicture}[x=0.95cm,y=1cm,font=\small]
\definecolor{vert}{RGB}{53,102,81}
\definecolor{bleu}{RGB}{59,105,153}
\draw[->,gray,thick] (-2.7,0) -- (2.8,0);
\foreach \x in {-2,-1,0,1,2} {
  \draw[gray] (\x,-0.09) -- (\x,0.09);
  \node[below] at (\x,-0.1) {$\x$};
}
\draw[fill=vert!12,draw=vert,rounded corners=2pt] (-0.3,0.2) rectangle (0.3,0.7);
\fill[vert] (-0.2,0.16) circle (0.07);
\fill[vert] (0.2,0.16) circle (0.07);
\node[above,text=vert] at (0,0.85) {Robot au d\'epart};
\draw[->,very thick,vert] (0.15,1.65) -- (2.1,1.65)
  node[midway,above,align=center] {A : $+1$ case\\2 unit\'es};
\draw[->,very thick,bleu] (-0.15,1.65) -- (-2.1,1.65)
  node[midway,above,align=center] {R : $-1$ case\\1 unit\'e};
\node[below,align=center] at (0,-0.65) {P : rester sur place\\0 unit\'e d'\'energie};
\end{tikzpicture}''',
    'recharge': r'''% Recharge : de 2 à au moins 8 unités
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
\definecolor{vert}{RGB}{53,102,81}
\foreach \x/\niveau/\temps in {0/2/0,2/5/1,4/8/2} {
  \fill[vert!25] (\x,0) rectangle (\x+0.8,\niveau/5);
  \draw[thick,vert] (\x,0) rectangle (\x+0.8,2);
  \draw[thick,vert] (\x+0.25,2) -- (\x+0.25,2.1) -- (\x+0.55,2.1) -- (\x+0.55,2);
  \node at (\x+0.4,0.3) {$\niveau$};
  \node[below] at (\x+0.4,-0.15) {$t=\temps$ min};
}
\draw[->,thick,vert] (0.95,1) -- (1.85,1) node[midway,above] {$+3$};
\draw[->,thick,vert] (2.95,1) -- (3.85,1) node[midway,above] {$+3$};
\draw[dashed,gray] (-0.2,1.6) -- (5,1.6);
\node[above,align=center] at (2.4,2.4) {Capacit\'e : 10\quad Cible : 8};
\node[below,text=vert] at (2.4,-0.8) {La cible est atteinte apr\`es 2 minutes.};
\end{tikzpicture}''',
    'execution': r'''% APAR : s’arrêter avant la commande impossible
\begin{tikzpicture}[font=\small,
etat/.style={draw,rounded corners=3pt,minimum width=2.8cm,minimum height=0.8cm,align=center},
fleche/.style={->,thick}]
\definecolor{vert}{RGB}{53,102,81}
\definecolor{rouge}{RGB}{160,63,48}
\node[etat,draw=vert,fill=vert!8] (debut) at (0,0) {D\'epart\\position 10 ; \'energie 3};
\node[etat,draw=vert,fill=vert!8] (avance) at (0,-1.7) {A ex\'ecut\'ee\\position 11 ; \'energie 1};
\node[etat,draw=vert,fill=vert!8] (pause) at (0,-3.4) {P ex\'ecut\'ee\\position 11 ; \'energie 1};
\node[etat,draw=rouge,fill=rouge!6] (arret) at (0,-5.1) {A refus\'ee : $1<2$\\Arr\^et d\'efinitif};
\draw[fleche,vert] (debut) -- (avance) node[midway,right] {co\^ut 2};
\draw[fleche,vert] (avance) -- (pause) node[midway,right] {co\^ut 0};
\draw[fleche,rouge] (pause) -- (arret) node[midway,right] {\'energie insuffisante};
\node[align=center,text=rouge] at (0,-6.3) {R n'est jamais essay\'ee.};
\node[align=center,text=vert] at (0,-7.1) {Pr\'efixe ex\'ecut\'e : AP};
\end{tikzpicture}''',
    'fonctions': r'''% Les fonctions se construisent les unes sur les autres
\begin{tikzpicture}[font=\small,
bloc/.style={draw,rounded corners=2pt,align=center,inner sep=6pt},
lien/.style={->,thick,draw=black!55}]
\definecolor{vert}{RGB}{53,102,81}
\node[bloc] (cout) at (0,0) {Q1\\\texttt{cout\_action}};
\node[bloc] (possible) at (0,-1.35) {Q2\\\texttt{action\_possible}};
\node[bloc,draw=vert,fill=vert!8] (prefixe) at (0,-2.7) {Q9\\\texttt{prefixe\_executable}};
\node[bloc] (position) at (-1.9,-4.2) {Q10\\\texttt{position\_finale}};
\node[bloc] (energie) at (1.9,-4.2) {Q11\\\texttt{energie\_restante}};
\node[bloc,draw=vert,fill=vert!8] (bilan) at (0,-5.8) {Q12\\\texttt{bilan\_mission}};
\draw[lien] (cout) -- (possible);
\draw[lien] (possible) -- (prefixe);
\draw[lien] (prefixe) -- (position);
\draw[lien] (prefixe) -- (energie);
\draw[lien] (position) -- (bilan);
\draw[lien] (energie) -- (bilan);
\end{tikzpicture}''',
}


def diagram(name):
    caption = '\nUne flèche signifie que la fonction du bas utilise celle du haut. Cette vue est simplifiée : tous les appels à réutiliser restent indiqués dans chaque question.\n' if name == 'fonctions' else ''
    return '\n\n```tikz\n' + DIAGRAMS[name] + '\n```\n' + caption + '\n'
