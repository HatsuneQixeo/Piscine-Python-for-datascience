def callLimit(limit: int):
    """Decorator for setting limits on function calls"""
    count = 0

    def callLimiter(function):
        """The decorator call"""

        def limit_function(*args, **kwargs):
            """Limit the amount of time given function is called"""

            nonlocal count

            if count >= limit:
                print(f"Error: function {function.__name__} at {function}",
                      "called too many times")
                return
            count += 1
            return function(*args, **kwargs)
        return limit_function
    return callLimiter

# class callLimit:
#     """Decorator class for setting limits on function calls"""

#     def __init__(self, limit: int):
#         """callLimit constructor"""
#         self.limit = limit
#         self.count = 0

#     def __call__(self, function):
#         """Parantheses Overload"""
#         def limit_function(*args, **kwargs):
#             """Limit the amount of time given function is called"""
#             if self.count >= self.limit:
#                 print(f"Error: function {function.__name__} at {function}",
#                       "called too many times")
#                 return
#             self.count += 1
#             return function(*args, **kwargs)
#         return limit_function
