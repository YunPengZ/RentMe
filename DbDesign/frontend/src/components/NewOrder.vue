<template>
  <div>
    <el-row class="row" type="flex" justify="center">
      <el-col :span="16">
        <el-steps :center="true" :active="activeStep" finish-status="success">
          <el-step title="步骤 1" description="填写用户的相关信息"></el-step>
          <el-step title="步骤 2" description="选择车型的相关信息"></el-step>
          <el-step title="步骤 3" description="选择相应车型的车辆"></el-step>
          <el-step title="步骤 4" description="支付押金"></el-step>
        </el-steps>
      </el-col>
    </el-row>
    <el-row class="row" type="flex" justify="center">
      <el-col :span="16">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
      activeStep: 3
    }
  },
  computed: {
  }
}
</script>
<style scoped>
  .row{
    margin-top: 50px;
  }
</style>
