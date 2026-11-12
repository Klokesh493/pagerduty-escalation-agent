"""Offline PagerDuty-style escalation recommendations."""
import argparse


def recommend(age, deadline, acknowledged):
    if age < 0 or deadline <= 0:
        raise ValueError("age must be nonnegative and deadline positive")
    if acknowledged:
        return "acknowledged"
    return "escalate" if age >= deadline else "wait"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--age", type=int, default=8)
    parser.add_argument("--deadline", type=int, default=5)
    parser.add_argument("--acknowledged", action="store_true")
    args = parser.parse_args()
    try:
        print(recommend(args.age, args.deadline, args.acknowledged))
    except ValueError as error:
        parser.error(str(error))
