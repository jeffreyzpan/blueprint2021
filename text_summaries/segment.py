import re

def segment(text):
    '''
    Segments long text into multiple paragraphs.
    Args:
        text (str): input text

    Returns:
        List[str]: list of paragraphs
    '''
    #paragraphs = text.split('\n \n')
    paragraphs = re.split('\n\n|\n \n', text)
    return paragraphs
