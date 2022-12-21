def quotes_list():
    with open("quotes.csv", 'r') as f:
        """
        returns cleared quotes list
        side note:
        opening file in 'w' mode creates new file,
         if file exists it truncate it(makes new one anyway)"""
        data = f.readlines()
        clear_list = []
        for line in data:
            clear_list.append(line.strip())
        return clear_list
