import minedojo


if __name__ == "__main__":
    env = minedojo.make(
        task_id="combat_spider_plains_leather_armors_diamond_sword_shield",
        image_size=(288, 512),
        world_seed=123,
        seed=42,
    )

    print(f"[INFO] Create a task with prompt: {env}")

    env.reset()
    for _ in range(100):
        obs, reward, done, _, info = env.step(env.action_space.no_op())
    env.close()

    print("[INFO] Installation Success")
