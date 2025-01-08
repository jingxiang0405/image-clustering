<template>
    <div>
        <button @click="toggleFrame">Toggle Frame</button>
    </div>
</template>

<script>
export default {
    name: "SideBar",
    methods: {
        toggleFrame() {
            this.$emit("toggle-frame")
        }
    }
}
</script>

<style scoped>
</style>