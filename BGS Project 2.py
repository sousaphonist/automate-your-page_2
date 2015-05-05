concepts = [['Programming Overview', 'You cannot use normal language to tell a computer what you want it to do, due to inherent ambiguity in most (if not all) natural languages. For example, does "bi-weekly" mean twice a week or every two weeks? For this reason a computer will only execute what it sees; it cannot read errors and determine what was actually meant.'],
['How to Program', "Whether it's HTML, Python, Java, or some other programming language, a computer can only interpret instructions, known as code, in a form it can interpret."],
['HTML', '"Hypertext Markup Language", or "HTML", is best-suited for very simple and direct commands, like displaying text. To add color and style to the way things are displayed, a "Cascading Style Sheet", or "CSS", is often included as a separate yet connected file.'],
['Python', 'Python is better when more complex coding is required. It allows for the creation of lists - where multiple individual "elements" may be placed, allowing for the manipulation of any or all of them at the same time. This is done through another innovation Python has over HTML: loops.'],
['Loops', '''Loops allow the computer to interpret the code and made decisions, either when to execute the code or to execute it multiple times. "If" loops only execute if a specified condition exists. An "else" clause may be added in the even that it's not. "While" loops will continuously execute their code so long as the condition exists. And "for" loops execute thier code for every element in the input list.'''],
['Functions', 'Whichever programming language is used, they all rely heavily on the use of "functions". Sometimes also called "processes" or "algorithms", funtions give simple, direct names to complex, multi-line code. In this way, you can easily run the same code multiple times for different inputs simply by calling up the correct function.']]
def get_html(list):
	html = '''<head>
  				<title>BGS Project</title>
  				<link rel="stylesheet" href="BGS-style.css">
			</head>
			<body>
				<h1>Important Concepts</hi>
				<div class="lesson">'''
	end = '''
			</div>
		</div>'''
	for concept in list:
		html_addition = '''<div class="lesson">
					<div class="concept-tile">
					''' + concept[0] + '''
					</div>
					<div class="concept-description">
					''' + concept[1] +'''
					</div>
					</div>'''
		html = html + html_addition
	html = html + end
	return html

print get_html(concepts)