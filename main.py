from flask import Flask, render_template, request, Blueprint, send_from_directory,jsonify,abort

app = Flask(__name__, static_folder='project-ng/dist/project-ng')

angular = Blueprint('angular', __name__,
                    template_folder='project-ng/dist/project-ng')
app.register_blueprint(angular)


@app.route('/assets/<path:filename>')
def custom_static_for_assets(filename):
    return send_from_directory('project-ng/dist/project-ng/assets', filename)


@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('project-ng/dist/project-ng/', filename)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
