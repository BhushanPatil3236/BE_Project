<template>
  <v-app>
    <div id="app">
      <div id="nav">
        <v-app-bar app color="primary" dark>
          <div class="d-flex align-center">
            <v-img
              alt="Vuetify Logo"
              class="shrink mr-2"
              contain
              src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
              transition="scale-transition"
              width="40"
            />

            <v-card-text>
              <h1 class="appname"> Food Estimator </h1>
            </v-card-text>
          </div>

          <v-spacer></v-spacer>

          <div v-if="isDisabled">
            <v-btn to="/" class="ma-1" >
              Home
            </v-btn>
            <v-btn to="/estimator" class="ma-1" >
              Calorie-Estimation
            </v-btn>
            <v-btn to="/form" class="ma-1" >
              Food-Nutrition
            </v-btn>
            <v-btn to="/data" class="ma-1" >
              Results
            </v-btn>
            <v-btn to="/account" class="ma-1" >
              My Account
            </v-btn>
          </div>
          <v-btn to="/auth" class="ma-1" v-else> Login </v-btn>
        </v-app-bar> 
      </div>
      <v-main>
        <router-view> </router-view>
        <!-- <div class="chatbot">
          <ChatBot />
        </div> -->

      </v-main>
      <v-footer app bottom fixed class="justify-center" color="#292929" height="100">
        <div
          class="title font-weight-light grey--text text--lighten-1 text-center"
        >
          &copy; {{ new Date().getFullYear() }} — Food Estimator — Made with 💜 by
          Our Team
        </div>
      </v-footer>
    </div>
  </v-app>
</template>

<script>
import Vue from "vue";
// import ChatBot from "./views/ ChatBot.vue"

export default {
  name: "App",
  components: {
    // ChatBot
  },

  data: () => ({
    //
  }),
  computed: {
    isDisabled() {
      return Vue.$cookies.isKey("token");
    }
  }
};
</script>

<style>

.chatbot{
  align-self: flex-end;
}
.appname{
  padding-top: 20px;
  font-size: 20px;
}

h1 {
  font-weight: 800;
  font-size: 18px;
  letter-spacing: 4px;
  margin: 0 0 1em 0;
  text-transform: uppercase;
}

h2 {
  margin: 0 0 1em 0;
  line-height: 22px;
  letter-spacing: 2px;
  font-size: 14px;
  font-weight: 800;
  text-transform: uppercase;
}

h3 {
  margin: 0 0 1em 0;
  letter-spacing: 2px;
  line-height: 22px;
  font-size: 16px;
  font-weight: 800;
  text-transform: uppercase;
}

p {
  line-height: 22px;
  margin: 0 0 1em 0;
  font-size: 18px;
  /* color: #303030; */
}
.contact-line {
  display: flex;
  margin: 0 auto;
  align-items: center;
}
.contact {
  padding-left: 1em;
  margin: 0.25em;
}
.experience-section {
  margin-bottom: 2em;
}
.experience-section:last-child {
  margin-bottom: 0;
}
.work-position-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.education-section {
  margin-bottom: 2em;
}
.education-section:last-child {
  margin-bottom: 0;
}
.chart{
  text-align: center;
  font-size: 12px;
  padding: 0px;
  margin: 0px;
}
.dates{
  margin: 0 0 1em 0;
  line-height: 22px;
  letter-spacing: 0px;
  font-size: 14px;
  font-weight: 900;
  text-transform: uppercase;
  color: #87CEEB;
}
</style>