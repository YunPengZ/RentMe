<template>
  <div id="app">
    <el-row>
      <router-view class="view-top"name="top"></router-view>
    </el-row>
    <el-row>
      <router-view class="view-mid"></router-view>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
div {
  height: 100%;
}
</style>
