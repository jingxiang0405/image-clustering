<template>
    <div class="main">
        <SideBar @toggle-frame="handleToggleFrame" ref="sbRef" />
        <Home />
    </div>
</template>

<script setup>
import SideBar from './components/SideBar.vue';
import Home from './components/Home.vue'
import { ref } from 'vue';

const sbRef = ref(null)

function handleToggleFrame() {
    sbRef.value.toggleFrame()
}



</script>

<style scoped>

.main{
    display: flex;
}
</style>