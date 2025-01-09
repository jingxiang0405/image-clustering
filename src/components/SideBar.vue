<template>
    <div class="sidebar">
        <button @click="toggleFrame">Toggle Frame</button>
        <div>
            <h3>Filters</h3>
            <div v-for="(theme, index) in themes" :key="index">
                <input type="checkbox" :id="`theme-${index}`" :value="theme" v-model="selectedThemes"
                    @change="emitFilter" />
                <label :for="`theme-${index}`">{{ theme }}</label>
            </div>
            <div v-for="(tag, index) in tags" :key="index">
                <input type="checkbox" :id="`tag-${index}`" :value="tag" v-model="selectedTags" @change="emitFilter" />
                <label :for="`tag-${index}`">{{ tag }}</label>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "SideBar",

    props: {
        themes: {
            type: Array,
            required: true
        },
        tags: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            selectedThemes: [],
            selectedTags: []
        };
    },
    methods: {
        toggleFrame() {
            this.$emit("toggle-frame")
        },

        emitFilter() {
            this.$emit('filter-images', {
                themes: this.selectedThemes,
                tags: this.selectedTags
            });
        }
    }
}
</script>

<style scoped>
.sidebar {
    display: block;
    width: 3vw;
    height: 100vh;
}
</style>