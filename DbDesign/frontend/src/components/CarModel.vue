<template>
  <div>
    <el-row>
      <el-card>
        <el-col :span="12">
          <el-form :model="ruleForm" label-width="100px">
            <el-form-item :label="车型">
              <template>
                <el-checkbox-group v-model="ruleForm.car_type" @change="handleCheckedCitiesChange">
                  <el-checkbox v-for="car_type in options['car_type']" :label="car_type" :key="car_type">{{car_type}}</el-checkbox>
                </el-checkbox-group>
              </template>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="12">
        </el-col>
      </el-card>
    </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
      options: {
        car_type: ['商务车', 'SUV', 'ETC']
      },
      ruleForm: {
        car_type: []
      }
    }
  },
  methods: {
    handleCheckAllChange (event) {
    },
    handleCheckedCitiesChange (value) {
      let checkedCount = value.length
      this.checkAll = checkedCount === this.options['car_type'].length
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.options['car_type'].length
    }
  }
}
</script>
<style scoped>
</style>
