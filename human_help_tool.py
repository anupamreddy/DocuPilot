from chroma_tools import store_in_chroma

def need_human_help(question: str) -> str:
    """ This tool helps you to get more information from user. this will take your question and returns users answer."""
    answer = input("Need your help! :: \n" + question + " ::")
    store_in_chroma("Question :: " + question + "\n Answer :: " + answer)
    return answer