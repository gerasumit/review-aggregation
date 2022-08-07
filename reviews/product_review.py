class ProductReview:
    author: str
    review: str
    reviewed_at: str
    meta: str

    def __init__(self, author: str, review: str, reviewed_at: str, meta: str):
        self.author = author
        self.review = review
        self.reviewed_at = reviewed_at
        self.meta = meta