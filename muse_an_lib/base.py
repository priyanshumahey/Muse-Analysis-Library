class Validate:
    """
    Validates if the dataset is in correct format.

    :param inpt: The input
    :type inpt: [[x, [y,z]],[x, [y,z]]]
    """
    
    def __init__(self, inpt):
        self.inpt = inpt
    
    def Valid(museInput):
        """
        Checks to see if the inpt is in the valid format

        :param museInput: Output from the muse headset
        :type museInput: [[x, [y,z]],[x, [y,z]]]

        :return: if the input is valid or not
        :rtype: boolean
        """
        val = True

        for i in range(len(museInput)):
            if len(museInput[i]) != 2 or len(museInput[i][1]) != 5:
                val = False
        
        return val


        