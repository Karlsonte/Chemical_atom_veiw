import pygame
import math
import random

from chemical_elements import get_element_info, orbitals

def get_neutrons(atomic_number, atomic_mass):
    return int(round(atomic_mass)) - atomic_number

def get_electron_configuration(atomic_number, nuclear_radius):
    configuration = []
    remaining_electrons = atomic_number
    for orbital, max_electrons, radius, speed in orbitals:
        if remaining_electrons <= 0:
            break
        electrons_in_orbital = min(remaining_electrons, max_electrons)
        configuration.append((electrons_in_orbital, (radius+nuclear_radius), speed))
        remaining_electrons -= electrons_in_orbital
    return configuration

def generate_angles(electron_configuration):
    angles_by_level = []
    for electrons, _, _ in electron_configuration:
        angles = [random.uniform(0, 360) for _ in range(electrons)]
        angles_by_level.append(angles)
    return angles_by_level

def calculate_min_diameter(particle_radius, num_particles):
    if num_particles == 1:
        return 2 * (particle_radius*1.125)
    particles_count = 1
    layer = 0
    while particles_count < num_particles:
        layer += 1
        particles_count += 6 * layer
    return 2 * ((particle_radius*1.125) * (layer + 1))

def core_radius(atomic_number, atomic_mass):
    nuclear_particle_count = int(round(atomic_mass)) + atomic_number
    nuclear_radius = int(round((calculate_min_diameter(4, nuclear_particle_count))))
    return int(round(nuclear_radius))

def sqrt_dist(nuclear_radius, screen_x, screen_y):
    theta = random.uniform(0, 2 * math.pi)
    r = nuclear_radius * math.sqrt(random.random())
    x = int((screen_x/2) + r * math.cos(theta))
    y = int((screen_y/2) + r * math.sin(theta))
    return [x, y]

def create_nucleon_positions(num_particles, particle_radius, center_x, center_y):
    if num_particles == 1:
        return [(center_x, center_y)]
    positions = [(center_x, center_y)]
    layer = 1
    particles_count = 1
    while particles_count < num_particles:
        angle_offset = math.pi / 3
        radius = layer * 2 * particle_radius * 1.125
        layer_particles = 6 * layer
        
        if particles_count + layer_particles > num_particles:
            remaining_particles = num_particles - particles_count
            angle_step = 2 * math.pi / remaining_particles
            for i in range(remaining_particles):
                angle = i * angle_step
                x = int(center_x + radius * math.cos(angle))
                y = int(center_y + radius * math.sin(angle))
                positions.append((x, y))
            break
        for i in range(layer_particles):
            if particles_count >= num_particles:
                break
            angle = i * angle_offset / layer
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            positions.append((x, y))
            particles_count += 1
        layer += 1
    return positions

def assign_colors(num_protons, num_neutrons):
    nucleons = ['proton'] * num_protons + ['neutron'] * num_neutrons
    random.shuffle(nucleons)
    return nucleons

def draw_atom_animation(element_name):
    atomic_number, atomic_mass = get_element_info(element_name)
    neutrons = get_neutrons(atomic_number, atomic_mass)
    nucleons = atomic_number + neutrons
    proton_radius = 4
    electron_radius = 2
    nuclear_radius = calculate_min_diameter(proton_radius, nucleons) / 2
    electron_configuration = get_electron_configuration(atomic_number, nuclear_radius)
    angles_by_level = generate_angles(electron_configuration)
    screen_size_corrector = electron_configuration[-1][1]
    if 57 <= atomic_number<=71 or 89 <= atomic_number <= 103:
        screen_x = int(round((800/294)*screen_size_corrector))
        screen_y = int(round((800/294)*screen_size_corrector))
    elif 112 < atomic_number:
        screen_x = int(round((625/294)*screen_size_corrector))
        screen_y = int(round((625/294)*screen_size_corrector))
    else:
        if screen_size_corrector < 120:
            screen_x = int(round((700/294)*120))
            screen_y = int(round((700/294)*120))
        else:
            screen_x = int(round((700/294)*screen_size_corrector))
            screen_y = int(round((700/294)*screen_size_corrector))
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption(f"{element_name} Atom")
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GREY = (100, 100, 100)
    center_x, center_y = screen_x // 2, screen_y // 2
    neutron_radius = proton_radius
    nucleon_positions = create_nucleon_positions(nucleons, proton_radius, center_x, center_y)
    nucleon_colors = assign_colors(atomic_number, neutrons)
    clock = pygame.time.Clock()
    running = True
    angle_offsets = [0] * len(electron_configuration)
    while running:
        screen.fill(BLACK)
        for pos, color in zip(nucleon_positions, nucleon_colors):
            particle_color = RED if color == 'proton' else WHITE
            pygame.draw.circle(screen, particle_color, pos, proton_radius)
        for _, radius, _ in electron_configuration:
            pygame.draw.circle(screen, GREY, (center_x, center_y), radius, 1)
        for level, ((electrons, radius, speed), angles) in enumerate(zip(electron_configuration, angles_by_level)):
            for angle in angles:
                moving_angle = angle + angle_offsets[level]
                electron_x = center_x + int(radius * math.cos(math.radians(moving_angle)))
                electron_y = center_y + int(radius * math.sin(math.radians(moving_angle)))
                pygame.draw.circle(screen, BLUE, (electron_x, electron_y), electron_radius)
            angle_offsets[level] += speed
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    draw_atom_animation("Oganesson")
