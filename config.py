from args import CalciumArgs, NeuronArgs, SimulationArgs, SynapticArgs

FigConfig: dict[str, SimulationArgs] = {
    "P": SimulationArgs(
    calcium=CalciumArgs(
        tau_ca = 33.961,
        c_pre = 0.775,
        c_post = 0.189,
        D = 8.668,
        extracellular_ca = 1.3,   # mM, can be changed to 1.5 or 1.8e or 3 mM
        a_pre = 0.111,
        a_post = 1.294,
        tau_ca_NMDA = 162.420,
        eta = 0.00436
    ),
    synapse=SynapticArgs(
        tau=150_000,
        rho_star=0.5,
        gamma_d=0.388,
        gamma_p=1.998,
        theta_d=1,
        theta_p=1.173,
        sigma=5.6568,
        up_down_strength_ratio=5,
        down_init_probability=0.5,
    ),
    neuron=NeuronArgs(
        spike_rate=0.1,
        pre_post_delay=0,
    ),
    simulation_time=60_000,
    step_time=0.1,
    ),

}
