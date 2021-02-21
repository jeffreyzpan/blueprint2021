from transformers import AutoTokenizer, AutoModel, pipeline, BartForConditionalGeneration

def summarize(paragraphs):
    '''
    Takes a set of paragraphs and returns a set of summaries.
    Args:
        paragraphs (List[str]): List of paragraphs
    
    Returns:
        List[str]: List of summaries corresponding to each paragraph
    '''
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)
    summaries = summarizer(paragraphs, min_length=5, max_length=1024)
    output_strs = [summary['summary_text'] for summary in summaries]

    return output_strs


### TEST THE SUMMARIZER ###
if __name__ == "__main__":
    inputs = ["The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
    "Phillips Academy Andover (also known as Andover or PA) is a co-educational university-preparatory school for boarding and day students in grades 9–12, along with a post-graduate (PG) year. The school is in Andover, Massachusetts, United States, 25 miles north of Boston. Phillips Academy has 1,131 students,[8] and is a highly selective school, accepting 13% of applicants with a yield as high as 86% (in 2017).[9] It is part of the Eight Schools Association and the Ten Schools Admissions Organization, as well as the G30 Schools Group."]
    summaries = summarize(inputs)
    print(summaries)
