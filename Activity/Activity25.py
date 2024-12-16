def act25():

    def list():

        courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete without index", "Delete with index"]

        courses.remove("Delete without index")
        courses.pop()
        courses.append("DHRS")
        courses.insert(0, "ABELS")

        print(courses)

    list()