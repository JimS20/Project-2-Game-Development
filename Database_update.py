


import psycopg2


def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname='Prj2' user= 'postgres' host = 'localhost'password = 'Zemamena1'")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the hiscore table
def upload_score(name, score):
    query = "UPDATE score SET sc=" + str(score) + " WHERE name = '" + name + "'"
    print(query)
    interact_with_database(query)


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM score")


# Downloads the top score from database
def download_top_score(score):
    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]

    return result
a = download_scores()
b = (a[1][0] + 1)
c = (a[0][0] + 1)

upload_score("jim",b)