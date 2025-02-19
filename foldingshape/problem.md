## Problem Statement

Bob has a large rectangular piece of roofing underlayment with dimensions H x W. The roof he's working on requires dimensions H2 x W2. He realized too late that he forgot the necessary tools to cut the underlayment down to the correct dimensions, so his only option is to fold the piece until it fits.

Bob is lazy and would like to know the minimum number of folds needed to get from dimensions H x W to H2 x W2. Since the roofing underlayment is rectangular, it's a valid option to rotate it 90 degrees before folding. For example if the original dimensions were given as 3 x 6, he may rotate the piece to 6 x 3 before folding. Rotating does not count as a fold. He can only fold the rectangle parallel to its edges, and after each fold, the dimensions must be integers.

## Input Format

The first line of input will be 2 space-separated integers H and W, the original dimensions of the roofing underlayment.

The second line of input will be 2 space-separated integers H2 and W2, the desired dimensions of the roofing underlayment.

## Output Format

Output a single integer -- the minimum number of folds to get from dimensions (H,W) to (H2,W2). It is always possible to get the desired dimensions.

## Constraints

1 <= W,H,W2,H2 <= 10,000,000
