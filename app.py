
from flask import Flask, render_template, request, session, redirect, url_for
import os
from levelup import batch_level_up
from currency import reduce_currency

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key')

# Home route redirects to currency tool
@app.route('/')
def home():
    return render_template('currency_tool.html', active_page='currency')

# Currency Tool
@app.route('/currency', methods=['GET', 'POST'])
def currency_tool():
    result = None
    if request.method == 'POST':
        try:
            gold = int(request.form.get('gold', 0))
            silver = int(request.form.get('silver', 0))
            brass = int(request.form.get('brass', 0))
            reduction_type = request.form.get('reduction_type', 'percent')
            if reduction_type == 'amount':
                reduce_gold = int(request.form.get('reduce_gold', 0))
                reduce_silver = int(request.form.get('reduce_silver', 0))
                reduce_brass = int(request.form.get('reduce_brass', 0))
                result = reduce_currency(gold, silver, brass, None, reduce_gold, reduce_silver, reduce_brass)
            else:
                reduction = float(request.form.get('reduction', 0))
                result = reduce_currency(gold, silver, brass, reduction)
        except Exception:
            result = 'error'
    return render_template('currency_tool.html', result=result, active_page='currency')



# Skill Level-Up Tool (Level Up)
@app.route('/levelup', methods=['GET', 'POST'])
def levelup():
    # Read skills from file
    with open('cleaned_skills.txt') as f:
        skills = [line.strip() for line in f if line.strip()]
    report = session.get('levelup_report')
    if request.method == 'POST':
        # Parse form data for all selected skills
        selected = request.form.getlist('skills')
        skills_data = []
        for skill in selected:
            current_level = int(request.form.get(f'level_{skill}', 0))
            career = request.form.get(f'career_{skill}') == 'on'
            checks = int(request.form.get(f'checks_{skill}', 1))
            skills_data.append({
                'skill': skill,
                'current_level': current_level,
                'career': career,
                'checks': checks
            })
        report = batch_level_up(skills_data)
        session['levelup_report'] = report
        return redirect(url_for('levelup'))
    # Clear results if requested
    if request.args.get('clear'):
        session.pop('levelup_report', None)
        return redirect(url_for('levelup'))
    return render_template('levelup.html', active_page='levelup', skills=skills, report=report)

# Placeholder Tool 3
@app.route('/tool3')
def tool3():
    return render_template('tool3.html', active_page='tool3')

if __name__ == '__main__':
    app.run(debug=True)
