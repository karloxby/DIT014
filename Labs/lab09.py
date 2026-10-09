
import random

scores = []

for i in range(0, 8):
    score = random.randint(-4, 8)
    scores.append(score)


def process_scores(scores, index, total):
    # Check whether the end of the list has been reached.
    if len(scores) != index:
        # Get current score
        score = scores[index]
        
        # If a score is negative, add twice its absolute value.
        if score < 0:
            score = 2 * (score * -1)

        total += score

        index += 1
        
        # Recursively process the next score.
        return process_scores(scores, index, total)

    else:
        return total


def main():
    total = process_scores(scores, 0, 0)
    print("\nPENALTY SCORE CALCULATOR\n")
    
    for score in scores:
        print(f"Score: {score:>4}")

    print("\nThe end of the list is reached!")
    print(f"Scores: {scores}\n")
    print(f"Total: {total}\n")


if __name__ == "__main__":
    main()

