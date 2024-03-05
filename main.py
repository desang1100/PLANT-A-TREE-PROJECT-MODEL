from flask import Flask,render_template,redirect,request,url_for,session,flash,get_flashed_messages
from flask_mysqldb import MySQLdb
from passlib.hash import sha256_crypt
from datetime import date,datetime, timedelta
import pandas as pd
app = Flask(__name__)

app.secret_key = "khareen1100"

def connection():
    try:
        conn = MySQLdb.connect(host= "localhost", user= "root", password = "", db ="plant_a_tree")
        return conn
    except Exception as e:
        return str(e)
    

#--------------------------------------------H O M E----------------------------------------------------->    
@app.route("/")
def home():
    return render_template("landing.html")




#----------------------------------------S I G N U P----------------------------------------------------->
@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup_process", methods=["POST"])
def signup_process():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    address = request.form['address']
    contact = request.form['contact']
    email = request.form['email']
    password = request.form['password']
    role = "user"

    conn = connection()
    if conn:
        cur = conn.cursor()
        hashed_password = sha256_crypt.hash(password)
        cur.execute("INSERT INTO tbl_users (firstname, lastname, address, contact, email, password,role) VALUES (%s, %s, %s, %s, %s, %s,%s)", (firstname, lastname, address, contact, email, hashed_password,role))
        conn.commit()

        return redirect(url_for("login"))
    else:
        return "Error: Could not connect to the database."




#----------------------------------------------L O G I N----------------------------------------------------->    
@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/login_process", methods=["POST"])
def login_process():
    email = request.form['email']
    password = request.form['password']

    conn = connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_users WHERE email = %s", (email,))
        user = cur.fetchone()

        if user:
            hashed_password = user[6]
            if sha256_crypt.verify(password, hashed_password):
                # Authentication successful, store session information
                session['user_id'] = user[0]
                return redirect(url_for("user_profile"))
            else:
                return "Incorrect password."
        else:
            return "Incorrect email."
    else:
        return "Error: Could not connect to the database."




#---------------------------------------------- L O G O U T    ----------------------------------------------------->

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    # Clear the user's session
    session.clear()
    return redirect(url_for("login"))  # Redirect to login page     





#----------------------------------------U S E R  P R O F I L E----------------------------------------------------->


@app.route("/user_profile")
def user_profile():
    if 'user_id' in session:
        user_id = session['user_id']

        conn = connection()
        if conn:
            cur = conn.cursor()

            # Fetch user information
            cur.execute("SELECT * FROM tbl_users WHERE id = %s", (user_id,))
            user = cur.fetchone()

            if user[7] == 'admin':
                # User is an admin, fetch all users and projects
                cur.execute("SELECT * FROM tbl_users")
                users = cur.fetchall()

                cur.execute("SELECT * FROM tbl_projects")
                projects = cur.fetchall()

                return render_template("admin_profile.html", user=user, users=users, projects=projects)
            else:
                # User is a regular user, fetch user's projects
                
                
                return render_template('userprofile.html',user=user)
        else:
            return "Error: Could not connect to the database."
    else:
        return redirect(url_for("login"))  # Redirect to login page if user is not logged in
    


@app.route("/user_projects")
def user_projects():
    if 'user_id' in session:
        user_id = session['user_id']
    else:
        # Handle when the user is not logged in
        return redirect(url_for("login"))

    conn = connection()
    if conn:
        cur = conn.cursor()

        # Fetch user information
        cur.execute("SELECT * FROM tbl_users WHERE id = %s", (user_id,))
        user = cur.fetchone()

        cur = conn.cursor()
        cur.execute("SELECT p.* FROM tbl_projects p INNER JOIN tbl_project_participants pp "
                    "ON p.id = pp.project_id WHERE pp.user_id = %s", (user_id,))
        projects = cur.fetchall()

        cur.close()
        conn.close()

        return render_template("user_projects_final.html", user=user, projects=projects)
    else:
        # Handle when there is an issue with the database connection
        return "Database connection error"




#----------------------------------------   A D D    P R O J E C T------------------------------------------------>


@app.route("/user_table")
def user_table():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_users")
    users = cur.fetchall()
    return render_template("admin_profile.html",users = users)

@app.route("/project_table")
def project_table():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_projects")
    projects = cur.fetchall()
    return render_template("project.html",projects = projects)
 
@app.route("/add_project_process", methods=["GET", "POST"])
def add_project_process():
    if request.method == "POST":
        project_name = request.form['project_name']
        project_desc = request.form['project_desc']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
        location = request.form['location']
        area_size = request.form['area_size']
        project_creation_date = datetime.now().date()
        status ="ongoing"
        project_scope = request.form['project_scope']
        soil_condition = request.form['soil_condition']
        weather_condition = request.form['weather_condition']


        if start_date <= end_date and start_date >= (datetime.now().date() + timedelta(days=5)):
            if 'user_id' in session:
                user_id = session['user_id']

                conn = connection()
                if conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tbl_projects (project_name, project_desc, start_date, end_date, location, area_size,  admin_id,project_creation_date,status,project_scope,soil_condition,weather_condition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (project_name, project_desc, start_date, end_date, location, area_size, user_id,project_creation_date,status,project_scope,soil_condition,weather_condition))
                    conn.commit()

                    return redirect(url_for("project_table"))
                else:
                    return "Error: Could not connect to the database."
            else:
                return redirect(url_for("login"))  # Redirect to login page if user is not logged in
        else:
            return "Invalid project dates. Please ensure the start date is not before today and at least 5 days in the future, and the end date is after the start date."
    
    return render_template("add_project.html")





#----------------------------------------  DELETE   USER  ------------------------------------------------>


@app.route("/delete_user/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    if 'user_id' in session:
        admin_id = session['user_id']

        conn = connection()
        if conn:
            cur = conn.cursor()

            # Check if the logged-in user is an admin
            cur.execute("SELECT role FROM tbl_users WHERE id = %s", (admin_id,))
            admin_role = cur.fetchone()

            if admin_role[0] == 'admin':
                # Delete the user with the given user_id
                cur.execute("DELETE FROM tbl_users WHERE id = %s", (user_id,))
                conn.commit()
                return redirect(url_for("user_profile"))
            else:
                return "Error: You do not have permission to perform this action."
        else:
            return "Error: Could not connect to the database."
    else:
        return redirect(url_for("login"))  # Redirect to login page if user is not logged in






#----------------------------------------   A D M I N  ------------------------------------------------>




@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if 'user_id' in session:
        admin_id = session['user_id']

        conn = connection()
        if conn:
            cur = conn.cursor()

            # Check if the logged-in user is an admin
            cur.execute("SELECT role FROM tbl_users WHERE id = %s", (admin_id,))
            admin_role = cur.fetchone()

            if admin_role[0] == 'admin':
                if request.method == "POST":
                    firstname = request.form['firstname']
                    lastname = request.form['lastname']
                    address = request.form['address']
                    contact = request.form['contact']
                    email = request.form['email']
                    
                    role = request.form['role']

                    # Update the user with the given user_id
                    cur.execute("UPDATE tbl_users SET firstname = %s, lastname = %s, address = %s, contact = %s, email = %s, role = %s WHERE id = %s", (firstname, lastname, address, contact, email, role, user_id))
                    conn.commit()
                    return redirect(url_for("user_profile"))

                # Fetch the user's information
                cur.execute("SELECT * FROM tbl_users WHERE id = %s", (user_id,))
                user = cur.fetchone()

                return render_template("edit_user.html", user=user)
            else:
                return "Error: You do not have permission to perform this action."
        else:
            return "Error: Could not connect to the database."
    else:
        return redirect(url_for("login"))  # Redirect to login page if user is not logged in


'''@app.route("/admin/projects", methods=["GET", "POST"])
def admin_projects():
    if 'user_id' in session:
        if request.method == "POST":
            project_id = request.form['project_id']
            new_status = request.form['status']

            # Update the project status in the database
            conn = connection()
            cur = conn.cursor()
            update_query = "UPDATE tbl_projects SET status = %s WHERE id = %s"
            cur.execute(update_query, (new_status, project_id))
            conn.commit()
        # Fetch the projects data from the database
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_projects")
        projects = cur.fetchall()
        conn.close()

        return render_template("admin_projects.html", projects=projects)

    return redirect(url_for("login"))


        

    



@app.route("/update_project_status", methods=["POST"])
def update_project_status():
    if 'user_id' in session and session['admin_id']:
        project_id = request.form['project_id']
        new_status = request.form['status']

        # Update the project status in the database
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE tbl_projects SET status = %s WHERE id = %s", (new_status, project_id))
        conn.commit()
        conn.close()

        return redirect(url_for("admin_projects"))
    
    return redirect(url_for("login"))'''

@app.route("/update_project_status", methods=["POST"])
def update_project_status():
    if 'user_id' in session :
        project_id = request.form['project_id']
        new_status = request.form['status']

        # Update the project status in the database
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE tbl_projects SET status = %s WHERE id = %s", (new_status, project_id))
        conn.commit()
        conn.close()

        return redirect(url_for("project_table"))

    return redirect(url_for("login"))

@app.route("/delete_project/<int:project_id>", methods=["GET","POST"])
def delete_project(project_id):
    if 'user_id' in session:
        # Delete the project from the database
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM tbl_projects WHERE id = %s", (project_id,))
        conn.commit()
        conn.close()

        return redirect(url_for("project_table"))

    return redirect(url_for("login"))


@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    if 'user_id' in session:
        # Retrieve the project from the database based on the project_id
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_projects WHERE id = %s", (project_id,))
        project = cur.fetchone()
        conn.close()

        if project:
            if request.method == "POST":
                # Update the project with the submitted form data
                project_name = request.form['project_name']
                project_desc = request.form['description']
                start_date = request.form['start_date']
                end_date = request.form['end_date']
                location = request.form['location']
                area_size = request.form['area_size']

                conn = connection()
                cur = conn.cursor()
                cur.execute("UPDATE tbl_projects SET project_name = %s, project_desc = %s, start_date = %s, end_date = %s, location = %s, area_size = %s WHERE id = %s",
                            (project_name, project_desc, start_date, end_date, location, area_size, project_id))
                conn.commit()
                conn.close()
            

                return redirect(url_for("project_table"))
            else:
                return render_template("edit_project.html", project=project)

    return redirect(url_for("login"))


@app.route("/view_project_details")
def view_project_status():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_projects")
    projects = cur.fetchall()
    return render_template("view_project.html",projects = projects)

 






#----------------------------------------   J O I N     P R O J E C T  ------------------------------------------------>

def get_available_projects():
    conn = connection()
    cur = conn.cursor()

    # Assuming there is a 'start_date' and 'end_date' column in the project table
    today = datetime.now().date()
    cur.execute("SELECT * FROM tbl_projects WHERE start_date <= %s AND end_date >= %s",
                (today, today))

    available_projects = cur.fetchall()

    return available_projects


def is_project_available(project):
    today = datetime.now().date()
    start_date = datetime.strptime(str(project[3]), "%Y-%m-%d").date()  # Assuming start_date is stored at index 3 in the project tuple
    end_date = datetime.strptime(str(project[4]), "%Y-%m-%d").date()  # Assuming end_date is stored at index 4 in the project tuple

    return start_date <= today <= end_date




@app.route("/join_project", methods=["GET", "POST"])
def join_project():
    
    if request.method == "POST":
        project_id = request.form['project_id']
        user_id = session['user_id']  # Assuming user ID is stored in the session
        
        if 'user_id' in session:
        # Retrieve the project from the database based on the project_id
            conn = connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM tbl_projects WHERE id = %s", (project_id,))
            project = cur.fetchone()
            conn.close()

            # Check if the project exists and is available on the scheduled date
            conn = connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM tbl_projects WHERE id = %s", (project_id,))
            project = cur.fetchone()

            if project and is_project_available(project):
                # Insert the participant data into tbl_project_participants
                cur.execute("INSERT INTO tbl_project_participants (project_id, user_id, role, join_date) VALUES (%s, %s, %s, %s)",
                            (project_id, user_id, 'Member', datetime.now().date()))
                conn.commit()

                flash("You have successfully joined the project!")
                return redirect(url_for("user_profile"))

    return redirect(url_for("display_available_projects"))




@app.route("/join_project_process", methods=["POST","GET"])
def join_project_process():
    if 'user_id' in session:
        user_id = session['user_id']
        project_id = request.form.get('project_id')

        # Check if the project exists and is available
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_projects WHERE id = %s", (project_id,))
        project = cur.fetchone()

        if project:
            column_names = [desc[0] for desc in cur.description]

            # Check if the project is already finished
            end_date_index = column_names.index('end_date')
            end_date = project[end_date_index]

            if end_date and end_date <= date.today():
                return 'The project you are trying to join has already finished.'

            # Check if the user is already a participant in the project
            cur.execute("SELECT * FROM tbl_project_participants WHERE project_id = %s AND user_id = %s", (project_id, user_id))
            existing_participant = cur.fetchone()

            if existing_participant:
                
                return "You have already joined this project.", "error"
           

            # Get the current number of participants for the project
            cur.execute("SELECT COUNT(*) FROM tbl_project_participants WHERE project_id = %s", (project_id,))
            current_participants = cur.fetchone()[0]

            # Increment the count
            current_participants += 1

            # Insert the user as a participant in the project
            insert_query = "INSERT INTO tbl_project_participants (project_id, user_id, join_date, no_participants) VALUES (%s, %s, %s, %s)"
            join_date = date.today()
            cur.execute(insert_query, (project_id, user_id, join_date, current_participants))
            conn.commit()

            cur.close()
            conn.close()

            return redirect(url_for('fetch_user_data', project_id=project_id))

    flash("You need to log in first.")
    return redirect(url_for("login"))


@app.route("/unjoin_project_process", methods=["POST"])
def unjoin_project_process():
    if 'user_id' in session:
        user_id = session['user_id']
        project_id = request.form.get('project_id')

        # Check if the user is currently a participant in the project
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_project_participants WHERE project_id = %s AND user_id = %s", (project_id, user_id))
        participant = cur.fetchone()

        if participant:
            # Delete the participant entry from tbl_project_participants
            delete_query = "DELETE FROM tbl_project_participants WHERE project_id = %s AND user_id = %s"
            cur.execute(delete_query, (project_id, user_id))
            conn.commit()

            cur.close()
            conn.close()

            return redirect(url_for('user_projects'))

    return redirect(url_for("login"))







   








@app.route("/display_available_projects")
def display_available_projects():
    conn = connection()
    cur = conn.cursor()
    
    # Assuming the columns in tbl_projects are id, project_name, project_desc, start_date, end_date, location, area_size, user_id, project_creation_date
    cur.execute("SELECT * FROM tbl_projects")
    available_projects = cur.fetchall()

    return render_template("join_project.html", available_projects=available_projects)



#--------------NAIVE BAYES------------------------------>

@app.route("/fetch_user_data/<int:project_id>")
def fetch_user_data(project_id):
    conn = connection()
    cur = conn.cursor()

    # Fetch project participants count
    cur.execute("SELECT COUNT(*) as participant_count FROM tbl_project_participants WHERE project_id = %s", (project_id,))
    participant_count = cur.fetchone()[0]

    # Fetch project data from tbl_project
    cur.execute("SELECT id, area_size, project_scope, soil_condition, weather_condition FROM tbl_projects WHERE id = %s", (project_id,))
    project_data = cur.fetchone()

    if project_data:
        # Modify area size value
        area_size = int(project_data[1])
        if area_size < 2000:
            area_size_category = "very small"
        elif 2000 <= area_size < 4000:
            area_size_category = "small"
        elif 4000 <= area_size < 8000:
            area_size_category = "medium"
        elif 8000 <= area_size <= 10000:
            area_size_category = "large"
        else:
            area_size_category = "very_large"

        # Modify participant count value
        if participant_count < 51:
            participant_count_category = "very_small"
        elif 51 <= participant_count < 100:
            participant_count_category = "_small"
        elif 100 <= participant_count < 200:
            participant_count_category = "_medium"
        elif 200 <= participant_count < 500:
            participant_count_category = "_large"
        else:
            participant_count_category = "very_large"

        # Create the result string
        result = [area_size_category,project_data[2],project_data[3],project_data[4],participant_count_category]
        print(result)
        #------------------------------------------------------------------------------------>>>>>>>>>>>>
        


    data=pd.read_csv('datanew.csv')
    data

    data['Time'].value_counts()
    A=10/49
    B=12/49
    C=9/49
    D=9/49
    E=9/49

    print(A)
    print(B)
    print(C)
    print(D)
    print(E)

    pd.crosstab(data['Area Size'], data['Time'])

    large_A = 3/10
    medium_A = 3/10
    small_A = 4/10
    verylarge_A = 0
    verysmall_A = 0


    large_B = 3/12
    medium_B = 3/12
    small_B = 5/12
    verylarge_B = 0
    verysmall_B = 1/12

    large_C = 2/9
    medium_C = 5/9
    small_C = 1/9
    verylarge_C = 1/9
    verysmall_C = 0

    large_D = 0
    medium_D = 1/9
    small_D = 1/9
    verylarge_D = 4/9
    verysmall_D = 3/9


    large_E = 2/9
    medium_E = 0
    small_E = 0
    verylarge_E = 2/9
    verysmall_E = 5/9

    pd.crosstab(data['Project Scope'],data['Time'])

    agroforestry_A = 7/10
    reforestation_A = 3/10
    urbanplanting_A = 0

    agroforestry_B = 3/12
    reforestation_B = 4/12
    urbanplanting_B = 5/12

    agroforestry_C = 3/9
    reforestation_C = 2/9
    urbanplanting_C = 4/9

    agroforestry_D = 6/9
    reforestation_D = 1/9
    urbanplanting_D = 2/9

    agroforestry_E = 0/9
    reforestation_E = 5/9
    urbanplanting_E = 4/9


    pd.crosstab(data['Soil Condition'],data['Time'])

    fair_A = 1/10
    good_A = 5/10
    poor_A = 4/10

    fair_B = 3/12
    good_B = 6/12
    poor_B = 3/12

    fair_C = 5/9
    good_C = 1/9
    poor_C = 3/9

    fair_D = 2/9
    good_D = 7/9
    poor_D = 0

    fair_E = 8/9
    good_E = 1/9
    poor_E = 0/9

    pd.crosstab(data['weather condition'],data['Time'])

    cloudy_A = 6/10
    rainy_A = 1/10
    sunny_A = 3/10

    cloudy_B = 3/12
    rainy_B = 4/12
    sunny_B = 5/12

    cloudy_C = 1/9
    rainy_C = 5/9
    sunny_C = 3/9

    cloudy_D = 5/9
    rainy_D = 2/9
    sunny_D = 2/9

    cloudy_E = 1/9
    rainy_E = 3/9
    sunny_E = 5/9

    pd.crosstab(data['participant'],data['Time'])

    _large_A = 3/10
    _medium_A= 2/10
    _small_A = 5/10
    very_large_A= 0
    very_small_A = 0

    _large_B = 2/12
    _medium_B= 3/12
    _small_B = 5/12
    very_large_B= 0
    very_small_B = 2/12

    _large_C = 3/9
    _medium_C= 5/9
    _small_C = 1/9
    very_large_C= 0
    very_small_C = 0

    _large_D = 4/9
    _medium_D= 1/9
    _small_D = 1/9
    very_large_D= 0
    very_small_D = 3/9

    _large_E = 3/9
    _medium_E= 0
    _small_E = 0
    very_large_E= 1/9
    very_small_E = 5/9


        # Initialize the lists
    data_list_A = []
    data_list_B = []
    data_list_C = []
    data_list_D = []
    data_list_E = []

    input_data = [result[0].lower(),result[1].lower(),result[2].lower(),result[3].lower(),result[4].lower(),]
    print(input_data)
        
    for input in input_data:


        if 'very small' == input:
            data_list_A.append(verysmall_A)
            data_list_B.append(verysmall_B)
            data_list_C.append(verysmall_C)
            data_list_D.append(verysmall_D)
            data_list_E.append(verysmall_E)
            print("m:",data_list_B)
        

        if 'small' == input:
            data_list_A.append(small_A)
            data_list_B.append(small_B)
            data_list_C.append(small_C)
            data_list_D.append(small_D)
            data_list_E.append(small_E)
        

        if 'medium' == input:
            data_list_A.append(medium_A)
            data_list_B.append(medium_B)
            data_list_C.append(medium_C)
            data_list_D.append(medium_D)
            data_list_E.append(medium_E)

        if 'large' == input:
            data_list_A.append(large_A)
            data_list_B.append(large_B)
            data_list_C.append(large_C)
            data_list_D.append(large_D)
            data_list_E.append(large_E)

        if 'very large' == input:
            data_list_A.append(verylarge_A)
            data_list_B.append(verylarge_B)
            data_list_C.append(verylarge_C)
            data_list_D.append(verylarge_D)
            data_list_E.append(verylarge_E)

        if 'reforestion' == input:
            data_list_A.append(reforestation_A)
            data_list_B.append(reforestation_B)
            data_list_C.append(reforestation_C)
            data_list_D.append(reforestation_D)
            data_list_E.append(reforestation_E)

        if 'urban planting' == input:
            data_list_A.append(urbanplanting_A)
            data_list_B.append(urbanplanting_B)
            data_list_C.append(urbanplanting_C)
            data_list_D.append(urbanplanting_D)
            data_list_E.append(urbanplanting_E)

        if 'agroforestry' == input:
            data_list_A.append(agroforestry_A)
            data_list_B.append(agroforestry_B)
            data_list_C.append(agroforestry_C)
            data_list_D.append(agroforestry_D)
            data_list_E.append(agroforestry_E)

        if 'good' == input:
            data_list_A.append(good_A)
            data_list_B.append(good_B)
            data_list_C.append(good_C)
            data_list_D.append(good_D)
            data_list_E.append(good_E)

        if 'fair' == input:
            data_list_A.append(fair_A)
            data_list_B.append(fair_B)
            data_list_C.append(fair_C)
            data_list_D.append(fair_D)
            data_list_E.append(fair_E)

        if 'poor' == input:
            data_list_A.append(poor_A)
            data_list_B.append(poor_B)
            data_list_C.append(poor_C)
            data_list_D.append(poor_D)
            data_list_E.append(poor_E)

        if 'sunny' == input:
            data_list_A.append(sunny_A)
            data_list_B.append(sunny_B)
            data_list_C.append(sunny_C)
            data_list_D.append(sunny_D)
            data_list_E.append(sunny_E)

        if 'rainy' == input:
            data_list_A.append(rainy_A)
            data_list_B.append(rainy_B)
            data_list_C.append(rainy_C)
            data_list_D.append(rainy_D)
            data_list_E.append(rainy_E)

        if 'cloudy' == input:
            data_list_A.append(cloudy_A)
            data_list_B.append(cloudy_B)
            data_list_C.append(cloudy_C)
            data_list_D.append(cloudy_D)
            data_list_E.append(cloudy_E)

        if 'very_small' == input:
            data_list_A.append(very_small_A)
            data_list_B.append(very_small_B)
            data_list_C.append(very_small_C)
            data_list_D.append(very_small_D)
            data_list_E.append(very_small_E)

        if '_small' == input:
            data_list_A.append(_small_A)
            data_list_B.append(_small_B)
            data_list_C.append(_small_C)
            data_list_D.append(_small_D)
            data_list_E.append(_small_E)

        if '_medium' == input:
            data_list_A.append(_medium_A)
            data_list_B.append(_medium_B)
            data_list_C.append(_medium_C)
            data_list_D.append(_medium_D)
            data_list_E.append(_medium_E)

        if '_large' == input:
            data_list_A.append(_large_A)
            data_list_B.append(_large_B)
            data_list_C.append(_large_C)
            data_list_D.append(_large_D)
            data_list_E.append(_large_E)

        if 'very_large' == input:
            data_list_A.append(very_large_A)
            data_list_B.append(very_large_B)
            data_list_C.append(very_large_C)
            data_list_D.append(very_large_D)
            data_list_E.append(very_large_E)

    


    data_lists = [data_list_A, data_list_B, data_list_C, data_list_D, data_list_E]
    final_values = []

    for data_list in data_lists:
        result = 1
        for value in data_list:
            result *= value
        final_values.append(result)

    Final_A, Final_B, Final_C, Final_D, Final_E = final_values[0]*A, final_values[1]*B, final_values[2]*C, final_values[3]*D, final_values[4]*E

    print(data_list_A)
    print(data_list_B)
    print(data_list_C)
    print(data_list_D)
    print(data_list_E)

    print("Final A:",Final_A)
    print("Final B:",Final_B)
    print("Final C:",Final_C)
    print("Final D:",Final_D)
    print("Final E:",Final_E)

    highest_value = max(Final_A, Final_B, Final_C, Final_D, Final_E)

    if highest_value == Final_A:
        variable_name = "Final A"
        category = "0-1 Hour"
    elif highest_value == Final_B:
        variable_name = "Final B"
        category = "1-3 Hours"
    elif highest_value == Final_C:
        variable_name = "Final C"
        category = "3-5 Hours"
    elif highest_value == Final_D:
        variable_name = "Final D"
        category = "5-8 Hours"
    else:
        variable_name = "Final E"
        category = "8-12 Hours"

    print("The highest value is:", highest_value)
    print("Variable Name:", variable_name)
    print("Category:", category)

 # Update the time_completion column in tbl_projects
    
    # Update time_completion in tbl_project
    cur.execute("UPDATE tbl_projects SET time_completion = %s WHERE id = %s", (category, project_id))
    conn.commit()

  
        # Fetch project data from tbl_project based on the project ID
    select_query = "SELECT project_name, project_desc, start_date, location, area_size, status, project_scope, soil_condition, weather_condition, time_completion FROM tbl_projects WHERE id = %s"
    cur.execute(select_query, (project_id,))
    project_data = cur.fetchone()
    print(project_data)

    # Close the database connection
    cur.close()
    conn.close()

    # Render the HTML template with the project data
    return render_template('view_project.html', project_data=project_data)






        #------------------------------------------------------------------------------------>>>>>>>>>>>>




if __name__ == '__main__':
    app.run(debug=True)