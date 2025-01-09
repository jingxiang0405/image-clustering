<template>

    <div class="main">
        <SideBar @toggle-frame="handleToggleFrame" @filter-images="handleFilter(themes, tags)" :tags="tagArr" :themes="themeArr"/>
        <Board ref="boardRef" :images="images" />
    </div>
</template>

<script>

import SideBar from '../components/SideBar.vue';
import Board from '../components/Board.vue';
import { ref } from 'vue';
import * as d3 from 'd3'

export default {

    data() {
        return {
            boardRef: ref(null),
            images: [],
            themeSet: null,
            tagSet: null,
        }
    },
    async created() {
        this.themeSet = new Set();
        this.tagSet = new Set();
        let images = await d3.csv("../../data.csv")
        this.images = images.map((row) => {
            this.themeSet.add(row.theme);
            this.tagSet.add(row.tag);
            const newImage = {
                x: parseFloat(row.x) * 150,
                y: parseFloat(row.y) * 150,
                img_path: row.name,
                cluster: parseInt(row.cluster),
                theme: row.theme,
                tag: row.tag
            }

            return newImage
        })

        console.log(this.images)

    },

    methods: {
        handleToggleFrame() {
            console.log('handle')
            boardRef.value.toggleFrame()
        },
        handleFilter(themes, tags) {
            boardRef.value.filter(themes, tags)
        }
    },
    computed:{
        themeArr(){
            return Array.from(this.themeSet)
        },

        tagArr(){
            return Array.from(this.tagSet);
        }
    },
    components: {
        SideBar, Board
    }

}

</script>

<style scoped>
.main {
    padding: 0;
    display: inline-flex;
    justify-content: space-between;
}
</style>