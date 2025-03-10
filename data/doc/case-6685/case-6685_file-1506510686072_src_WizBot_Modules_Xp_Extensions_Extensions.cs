﻿using WizBot.Modules.Xp.Services;
using WizBot.Services.Database.Models;

namespace WizBot.Modules.Xp.Extensions
{
    public static class Extensions
    {
        public static (int Level, int LevelXp, int LevelRequiredXp) GetLevelData(this UserXpStats stats)
        {
            var baseXp = XpService.XP_REQUIRED_LVL_1;
            
            var required = baseXp;
            var totalXp = 0;
            var lvl = 1;
            while (true)
            {
                required = (int)(baseXp + baseXp / 4.0 * (lvl - 1));

                if (required + totalXp > stats.Xp)
                    break;

                totalXp += required;
                lvl++;
            }

            return (lvl - 1, stats.Xp - totalXp, required);
        }
    }
}