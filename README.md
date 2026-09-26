# 👗 Fashion Outfit Recommender

An outfit recommendation system that suggests visually and stylistically matching clothing items using deep learning image embeddings, with an interactive Streamlit app for live demos.

## Problem Statement

Most fresher-level recommender projects rely on tabular metadata (genre tags, ratings) rather than actual visual understanding. This project instead recommends **outfit pairings directly from product images** — given a top, it suggests matching bottoms, footwear, or accessories, using the *visual content* of the images themselves rather than manually labeled tags.

## Dataset

- [Fashion Product Images (Small)](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small) — Kaggle, ~44,000 product images with metadata (category, color, gender, article type)
- Filtered to ~37,000 relevant apparel/footwear/accessory items, sampled to a balanced 10,000-image subset (2,500 per outfit "slot") for computational feasibility

## Approach

1. **Data cleaning** — handled malformed CSV rows (unescaped commas in product names), filtered to outfit-relevant categories, mapped subcategories into four outfit "slots": `top`, `bottom`, `footwear`, `accessory`
2. **Feature extraction** — used a pretrained **ResNet50** (ImageNet weights, top layer removed, global average pooling) to convert each product image into a 2048-dimensional embedding vector
3. **Baseline recommender** — cosine similarity between embeddings to find visually similar items across outfit slots
4. **Limitation identified** — pure embedding similarity matched on overall image composition (pose, background, lighting) rather than true style compatibility, occasionally producing gender-mismatched or contextually odd results
5. **Rule-based refinement** — added gender-consistency filtering and basic color-clash rules on top of embedding similarity, meaningfully improving result quality (see comparison below)
6. **Interactive demo** — built a Streamlit app with a custom light, fashion-editorial theme, letting a user pick any item and get live recommendations for a chosen outfit slot

## Before vs After: Rule-Based Refinement

| Baseline (cosine similarity only) | With gender + color constraints |
|---|---|
| Occasionally recommended cross-gender items (e.g., a women's swimsuit for a men's t-shirt query) | All recommendations respect gender consistency |
| No color-logic awareness | Basic clash-avoidance applied |

## Tech Stack

- **Python**, **Pandas**, **NumPy**
- **TensorFlow/Keras** (ResNet50, pretrained on ImageNet)
- **scikit-learn** (cosine similarity)
- **Streamlit** (interactive web app)
- **Matplotlib / PIL** (visualization during development)

## Project Structure

```
├── app.py                  # Streamlit application
├── Project.ipynb           # Data exploration, embedding extraction, experimentation
├── sample_df.csv           # Metadata for the sampled 10,000-item subset
├── .streamlit/config.toml  # App theme configuration
└── requirements.txt
```

> **Note:** `embeddings.npy` (precomputed ResNet50 embeddings, ~80MB) is not committed to this repo due to GitHub's file size limits. It's generated locally by running `Project.ipynb` end-to-end (Step 7-9 in the notebook), which saves it into the project folder — required before running `app.py`.

## How to Run

1. Clone this repo
2. Download the [Fashion Product Images (Small) dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small) from Kaggle and place the `images/` folder in the project root
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run `Project.ipynb` to generate `embeddings.npy` (takes ~20-30 minutes on CPU)
5. Run the app:
   ```
   streamlit run app.py
   ```

## Limitations & Future Work

- Current matching is based on general visual similarity plus simple rule-based filters, not learned outfit compatibility
- **Planned improvement:** train a dedicated compatibility model (e.g., a Siamese network) on the [Polyvore Outfits dataset](https://github.com/xthan/polyvore-dataset), which contains real user-curated outfit combinations, to directly learn "what goes well together" rather than approximating it with rules
- Currently sampled to 10,000 images for feasibility; could scale to the full ~37,000-item dataset with more compute
- No quantitative offline evaluation (e.g., precision@k) yet — a next step would be manually labeling a small validation set of query-recommendation pairs to measure match quality numerically

## Author

Harshita Bansal — B.Tech CSE, Lovely Professional University
