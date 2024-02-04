from flask import Flask,request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY']= "chicken123"

debug = DebugToolbarExtension(app)

@app.route('/home')
def show_form():
    """printing all the form requirements inputs for creating a madlibs story"""
    return render_template('game_form.html', prompts = stories.story.prompts)

@app.route('/story')
def show_story():
    ans = request.args.to_dict()
    madlibs_final_result=stories.story.generate(ans)
    return render_template('story_page.html', story= madlibs_final_result)
