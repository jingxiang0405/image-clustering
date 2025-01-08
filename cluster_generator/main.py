import torch
import logging
import json
from torchvision.transforms import v2

# custom module
import image_loader
import model_factory
import kmeans
import output
import dimension

# Read configuration
with open("config.json", "r") as f:
    config = json.load(f)

kmeans_nclusters = config.get("kmeans_ncluster", 5)

image_directory = config.get("image_directory", "./image")
model_name = config.get("model", "vgg19")
output_csv = config.get("output_csv", "../data.csv")
dimension_reduction = config.get("dimension_reduction", "tsne")
image_directory = config.get("image_directory", "../images")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(filename)s %(levelname)s:%(message)s"
)


def main():
    # Logging

    logging.info("Loading Model...")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model_factory.create(model_name, device)
    # Define the image transform (resize, normalize)
    transform = v2.Compose(
        [
            v2.Resize((224, 224)),
            v2.ToImage(),
            v2.ToDtype(torch.float32, scale=True),
            v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    logging.info("Loading images...")
    images, image_names = image_loader.load_images_with_tag_from_directory(
        image_directory, transform, device
    )
    logging.info("Extracting features...")
    features = model_factory.extract_features(images, model)

    logging.info("Applying dimension reduction...")
    dr_result = dimension.reduce(features, dimension_reduction)

    # K-Means
    logging.info(f"Applying K-Means clustering with {kmeans_nclusters} clusters...")
    kmeans_labels = kmeans.apply_kmeans(features, nclusters=kmeans_nclusters)

    logging.info("Generating View Model(K-Means)")
    output.generate_view_model(
        image_names=image_names,
        results=dr_result,
        output=output_csv,
        clusters=kmeans_labels,
        )

    logging.info(f"HTML visualization saved to {output_csv}")


if __name__ == "__main__":
    main()
