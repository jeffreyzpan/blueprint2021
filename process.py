from text_summaries import summarize, segment

def process(image_path):
    ### 1: IMAGE SEGMENTATION ###

    ### 2: CAPTIONING ###

    ### 3: TEXT RECOGNITION ###

    ### 4: SUMMARIZATION ###
    text = "" # multi-paragraph text
    segmented_paragraphs = segment(paragraphs)
    summaries = summarize(segmented_paragraphs)

    ### 5: COMBINE RESULTS ###
    overall_desc = {'bullets': summaries, image_descs: []}

    return overall_desc
