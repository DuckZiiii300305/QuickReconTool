def load_targets(single, file):
    targets = []

    if single:
        targets.append(single.strip())

    if file:
        with open(file) as f:
            for line in f:
                if line.strip():
                    targets.append(line.strip())

    return list(set(targets))