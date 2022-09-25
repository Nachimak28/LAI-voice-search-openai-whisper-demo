from duckduckgo_search import ddg


def make_html(keywords, search_result_list):
    html0 = f"""
                <div style='margin-bottom: 10px; font-weight: bold; color: black; border-radius: 25px; background: white; text-align: center'>Transcribed Text: {keywords}</div>
            """
    html = (
        html0
        + "<div style='margin-top: 20px; display: flex; flex-wrap: wrap; justify-content: space-evenly'>"
    )
    for result_dict in search_result_list:
        html2 = f"""
                <div style='background: white; padding: 15'>
                    <a href='{result_dict.get('href', None)}' target='_blank' style='color: grey'>
                        <h1 style='color: blue'>{result_dict.get('title', None)}</h1>
                    </a>
                    <p style='color: black'>{result_dict.get('body', None)}</p>
                    </br>
                </div>
                """
        html = html + html2
    html += "</div>"
    return html


class Search:
    def __init__(
        self, region: str = "us-en", safesearch: str = "On", time="y", max_results=5
    ):
        self.region = region
        self.safesearch = safesearch
        self.time = time
        self.max_results = max_results

    def search(self, keywords: str):
        search_results = ddg(
            keywords,
            region=self.region,
            safesearch=self.safesearch,
            time=self.time,
            max_results=self.max_results,
        )

        # dummy results to quickly test and debug
        # search_results = [{'title': 'What Is The Answer Of 42? - Problem Solver X', 'href': 'https://problemsolverx.com/what-is-the-answer-of-42/', 'body': 'After calculating for 7.5 million years, Deep Thought came up with the answer. What is the meaning of 42? The meaning of life, the universe, and everything can be found in the number 42. Is 42 the perfect number? 42 isnt a perfect number. The following steps are used to determine if a number is a perfect number.'},
        # {'title': 'How is 42 the answer to Life, the universe and the everything?', 'href': 'https://9to5science.com/how-is-42-the-answer-to-life-the-universe-and-the-everything', 'body': 'This is not mathematics. It is a reference to The Hitchhikers Guide to the Galaxy by Douglas Adams (originally a series of radio plays, later a wildly popular series of books, also adapted as movies), in which it is a plot point that the answer to the ultimate question of life, the universe, and everything is known to be the number $42$ -- but unfortunately it is unknown which question the ...'}]

        return make_html(keywords, search_results)
