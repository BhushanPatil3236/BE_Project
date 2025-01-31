<template>
  <div>
    <v-parallax
      dark
      src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    >
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="text-h4 font-weight-thin mb-4">Form Details</h1>
          <h4 class="subheading">Welcome to nutrition diet prediction!</h4>
        </v-col>
      </v-row>
    </v-parallax>
    <v-card :loading="loading" class="mx-auto my-12" max-width="374">
      <v-container class="justify-center">
        <template slot="progress">
          <v-progress-linear
            color="primary"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>

        <v-card-title class="justify-center"
          >Find the best nutrition diet</v-card-title
        >

        <v-card-text>
          <template>
            <ValidationObserver ref="observer" v-slot="{ invalid }">
              <form @submit.prevent="Login">
                <ValidationProvider
                  name="Age"
                  rules="required|max:3"
                  v-slot="{ errors }"
                  :bails="true"
                >
                  <v-text-field
                    v-model=age
                    type="number"
                    :error-messages="errors"
                    label="Age"
                    required
                    counter
                    outlined
                    shaped
                    prepend-icon="mdi-email"
                    hide-details="auto"
                  />
                </ValidationProvider>

                <v-checkbox
                  v-model=diet
                  :label="`Veg / Non-veg: ${
                    diet.toString() === 'true'
                      ? 'Veg is selected'
                      : 'Non-veg is Selected'
                  }`"
                ></v-checkbox>

                <ValidationProvider
                  name="Height"
                  rules="required|max:3"
                  v-slot="{ errors }"
                  :bails="true"
                >
                  <v-text-field
                    v-model=height
                    type="number"
                    :error-messages="errors"
                    label="Height"
                    required
                    counter
                    outlined
                    shaped
                    prepend-icon="mdi-email"
                    hide-details="auto"
                  />
                </ValidationProvider>

                <ValidationProvider
                  name="Weight"
                  rules="required|max:3"
                  v-slot="{ errors }"
                  :bails="true"
                >
                  <v-text-field
                    v-model=weight
                    type="number"
                    :error-messages="errors"
                    label="Weight"
                    required
                    counter
                    outlined
                    shaped
                    prepend-icon="mdi-email"
                    hide-details="auto"
                  />
                </ValidationProvider>

                <div>
                  <v-spacer></v-spacer>
                  <v-btn class="ma-4" text @click="Submit" :disabled="invalid">
                    Submit
                  </v-btn>
                </div>
              </form>
            </ValidationObserver>
          </template>
        </v-card-text>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
export default {
  data: () => ({
    age: 0,
    diet: true,
    weight: 0,
    height: 0,
    token: Vue.$cookies.get("token")
  }),

  methods: {
    Submit() {
      this.$refs.observer.validate().then(success => {
        if (!success) {
          return;
        }

        axios({
          method: "POST",
          url: "http://127.0.0.1:8000/get-nutrition/",
          data: JSON.stringify({
            age: parseInt(this.age),
            diet: this.diet,
            weight: parseInt(this.weight),
            height: parseInt(this.height),
          }),
          headers: {
            "Content-Type": "application/json; charset=UTF-8",
            Authorization: `token ${this.token}`,
          }
        })
          .then(res => {
            console.log(res);
            alert("your personilized Nutrition is ready! click ok to continue.");
            this.$router.push("/data");
          })
          .catch(error => {
            alert(error);
            this.errored = true;
          });

        this.loading = true;
        setTimeout(() => (this.loading = false), 2000);
      });
    }
  }
};
</script>

<style></style>