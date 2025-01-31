<template>
  <div class="home">
        <v-parallax
      dark
      src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    >
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 font-weight-thin mb-4">Welcome to the Food Colorie Estimator and Nutrition Suggest</h1>
          <h4 class="subheading">Welcome check your personalized nutrition today!</h4>
        </v-col>
      </v-row>
    </v-parallax>
    <AboutView />
  </div>
</template>

<script>
import AboutView from './AboutView.vue'
export default {
  name: 'HomeView',
  components: {
    AboutView,
  }
}
</script>