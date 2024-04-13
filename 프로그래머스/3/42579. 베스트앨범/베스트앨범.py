from collections import defaultdict

def solution(genres, plays):
    answer = []
    songs_by_genre = defaultdict(lambda: [])
    plays_by_genre = defaultdict(lambda: 0)
    for i in range(len(genres)):
        songs_by_genre[genres[i]].append((plays[i], i))
        plays_by_genre[genres[i]] += plays[i]
    
    sorted_genres = sorted(plays_by_genre.items(), key=lambda x: x[1], reverse=True)
    for genre, _ in sorted_genres:
        sorted_songs = sorted(songs_by_genre[genre], key=lambda x: [-x[0], x[1]])
        answer.append(sorted_songs[0][1])
        if len(sorted_songs) > 1:
            answer.append(sorted_songs[1][1])
    
    return answer