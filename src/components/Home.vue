<template>
    <div>
        <div class="board">
            <div v-for="(image, i) in images" :key="i" class="image-container" :style="getImageStyle(image)"
                @mouseover="showTooltip(image.theme, image.tag, $event)" @mouseleave="hideTooltip">
                <img :src="image.img_path" :alt="image.tag" class="image" />
            </div>
            <div v-if="tooltip.visible" class="tooltip" :style="tooltipStyle">
                <div>{{ tooltip.theme }}</div>
                <div>{{ tooltip.text }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import * as d3 from 'd3'
export default {
    data() {
        return {
            images: [], // Load CSV data into this array
            showFrames: false,
            tooltip: {
                visible: false,
                theme: "",
                text: "",
                x: 0,
                y: 0
            }
        };
    },
    async created() {
        await d3.csv("../../data.csv").then((data) => {
            console.log(data)
            this.images = data.map(row => ({
                x: parseFloat(row.x)*150, // scale
                y: parseFloat(row.y)*150,
                img_path: row.name,
                cluster: parseInt(row.cluster),
                theme: row.theme,
                tag: row.tag
            }));
        })

        console.log(this.images)
    },
    computed: {
        tooltipStyle() {
            return {
                top: `${this.tooltip.y}px`,
                left: `${this.tooltip.x}px`,
            };
        }
    },
    methods: {

        toggleFrame() {
            this.showFrames = !this.showFrames;
        },
        getImageStyle(image) {
            const styles = {
                position: "absolute",
                top: `${image.y}px`,
                left: `${image.x}px`,
                width: '100%',
                height: '100%',
                border: this.showFrames ? `3px solid ${this.getClusterColor(image.cluster)}` : "none",

            };
            return styles;
        },
        getClusterColor(cluster) {
            const colors = ["red", "blue", "green", "orange", "purple", "brown", "pink", "yellow"];
            return colors[cluster % colors.length];
        },
        showTooltip(theme, tag, event) {
            this.tooltip.visible = true;
            this.tooltip.theme = theme;
            this.tooltip.text = tag;
            this.tooltip.x = event.pageX + 10;
            this.tooltip.y = event.pageY + 10;
        },
        hideTooltip() {
            this.tooltip.visible = false;
        }
    }
};
</script>

<style>
.board {
    width: 1000px;
    height: 1000px;
    overflow: auto;
    border: 1px solid #ccc;
}

.image-container {
    position: absolute;
    max-width: 50px;
    max-height: 50px;
}

.image {
    display: block;
    max-width: inherit;
    max-height: inherit;
}

.tooltip {
    position: absolute;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 5px;
    border-radius: 5px;
    pointer-events: none;
    font-size: 12px;
}
</style>