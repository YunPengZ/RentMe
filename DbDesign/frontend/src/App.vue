<template>
  <div id="app" class="maxheight">
    <el-row>
      <router-view name="top"></router-view>
    </el-row>
    <el-row class="maxheight">
      <router-view></router-view>
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
.maxheight {
  height: 100%;
}
</style>
