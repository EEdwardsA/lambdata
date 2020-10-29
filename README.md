# lambdata
A package that contains the following modules:

Assignment_module wrangles a dataframe.
    """
    This wrangle function counts null values and creates a train_test
    split based on your 'target' variable

    Before running this function, assign a column name to the variable "target"

    Params: a dataframe called "df"

    Outputs a tuple containing, in order, X, y, X_train, X_test, y_train, y_test
    
    """

Example_module creates 2 lists and 2 functions.
    """
    This module creates two short lists, colors and fav_numbers.

    This module creates two functions: clean_df which is currently blank, with a parameter "df", and increment which takes a numerical input as a parameter and returns that number plus 1.
    """

Oop_example contains examples of object-oriented programming.
    """
    Class Complex is a constructor for complex numbers
        Complex numbers have a real part and an imaginary part.
        
        Params: realpart, imagpart

        Method: "add" which takes as a parameter a second complex number.

    Class SocialMediaUser creates a class for a social media user.
        Params: name, location, upvotes(default=0)

        Methods: receive_upvotes, and is_popular (a user is popular if they have more  than 100 upvotes)

    Class MyDataFrame inherits all the traits of the Pandas Dataframe and adds a new method, num_cells, that returns the number of cells in the dataframe.

    Class Animal is a general representation of animals.
        Params: name, weight, diet_type

        Methods: run, which outputs a string about fast traveling, and eat, which outputs a string expressing appreciation for the food you've shared(param: a food item in string form)

    Class Sloth inherits the traits of class Animal and adds a new parameter, num_naps.
        Methods: run and say_something, which outputs a genuinely terrible pun.
    """

Lambda_test is full of unit tests for the above modules.



