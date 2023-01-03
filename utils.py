"""Project Utils."""

QUESTIONS_PER_PAGE = 10


def paginate_data(request, selection):
    """Paginates data based on the supplied input.
        Args:
            request (str): The request
            selection (any): current selection
        Returns:
            list: The paginated data
        """
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    items = [item.format() for item in selection]
    result = items[start:end]

    return result
