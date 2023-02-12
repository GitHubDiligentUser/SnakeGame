def update_file(instant_score: int, saved_high_score: int) -> int:
    if instant_score <= -1 or saved_high_score <= -1:
        raise ValueError('Score can not be under 0!')
    if instant_score > saved_high_score:
        """access the file"""
        file = open('high_scores.txt', 'w')
        file.write('high score: ' + str(instant_score))  # we convert integer to string
        file.close()
        saved_high_score = instant_score

    return saved_high_score
