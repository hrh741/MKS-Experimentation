function [out_tvalues]=gsh_hex_tri_L0_8(phi1, phi, phi2)

zvec = abs(phi) < 10e-17;
randvec = round(rand(size(zvec)));
randvecopp = ones(size(zvec)) - randvec;
phi = phi + (1e-7)*zvec.*(randvec - randvecopp);

out_tvalues = zeros(90, length(phi1));

t120 = cos(phi);
t114 = t120 ^ 2;
t81 = -0.18e2 * t114;
t353 = 0.1e1 + t81;
t84 = 0.1e1 - t120;
t154 = sqrt(t84);
t61 = 0.1e1 / t154;
t73 = exp((-1*i) * phi1);
t352 = t61 * t73;
t308 = (-1*i) * t154;
t72 = exp((i) * phi1);
t351 = t308 * t72;
t350 = (i) * t352;
t159 = t114 ^ 2;
t158 = t120 * t114;
t161 = t158 ^ 2;
t163 = t159 ^ 2;
t226 = 0.15e2 * t163 - 0.46e2 * t161 + 0.48e2 * t159 + t353;
t83 = 0.1e1 + t120;
t153 = sqrt(t83);
t165 = t153 * t83;
t166 = t83 * t165;
t289 = 0.3e1 / 0.64e2 * t120;
t349 = t166 * t289;
t109 = t120 * t161;
t348 = -0.6e1 * t109;
t347 = 0.7e1 * t109;
t111 = t120 * t159;
t346 = -0.4e1 * t111;
t345 = 0.2e1 * t114;
t85 = 0.7e1 * t114;
t344 = -0.6e1 * t120;
t343 = -0.3e1 * t120;
t342 = -0.2e1 * t120;
t341 = 0.5e1 * t120;
t340 = 0.6e1 * t120;
t339 = 0.2e1 * t158;
t338 = -0.3e1 * t159;
t337 = 0.5e1 * t159;
t336 = -0.7e1 * t163;
t335 = 0.4e1 * t163;
t107 = t120 * t163;
t334 = 0.20e2 * t107;
t333 = -0.21e2 * t111;
t332 = -0.14e2 * t111;
t331 = -0.10e2 * t114;
t330 = 0.10e2 * t114;
t329 = 0.15e2 * t114;
t328 = -0.38e2 * t158;
t327 = 0.21e2 * t158;
t326 = 0.22e2 * t158;
t325 = -0.20e2 * t159;
t324 = 0.20e2 * t159;
t323 = 0.35e2 * t159;
t146 = 3 * phi2;
t152 = 2 * phi1;
t93 = t152 + t146;
t27 = exp((2*i) * t93);
t147 = -3 * phi2;
t94 = t152 + t147;
t28 = exp((2*i) * t94);
t322 = (t27 + t28) * t325;
t45 = exp((-2*i) * t93);
t46 = exp((-2*i) * t94);
t321 = (t45 + t46) * t325;
t97 = phi1 + (2 * phi2);
t23 = exp((3*i) * t97);
t100 = phi1 - (2 * phi2);
t24 = exp((3*i) * t100);
t320 = (t23 + t24) * t326;
t319 = -0.1e1 - 0.5e1 * t159;
t318 = -0.1e1 + t161;
t317 = 0.1e1 + t159;
t316 = 0.1e1 + t161;
t66 = 0.5e1 * t114 - 0.1e1;
t314 = -0.1e1 + t330;
t313 = 0.5e1 - 0.30e2 * t114;
t49 = exp((-3*i) * t97);
t50 = exp((-3*i) * t100);
t312 = (t49 + t50) * t326;
t145 = 6 * phi2;
t150 = 5 * phi1;
t89 = t150 + t145;
t33 = exp((i) * t89);
t148 = -6 * phi2;
t90 = t150 + t148;
t34 = exp((i) * t90);
t311 = t33 * t330 + t34 * t331;
t39 = exp((-1*i) * t89);
t40 = exp((-1*i) * t90);
t310 = t39 * t330 + t40 * t331;
t95 = phi1 + t145;
t35 = exp((i) * t95);
t102 = phi1 + t148;
t36 = exp((i) * t102);
t309 = (t35 + t36) * t340;
t307 = t153 * t154;
t306 = t346 + 0.4e1 * t120;
t305 = t158 + 0.3e1 * t120;
t304 = (0.1e1 / 0.4e1*i) * t120;
t303 = t345 - t317;
t302 = 0.1e1 + t345 + t338;
t301 = 0.1e1 + 0.21e2 * t114 + 0.7e1 * t161;
t300 = 0.4e1 - 0.8e1 * t114 + 0.24e2 * t161;
t299 = (-1*i) * t307;
t298 = t120 * sqrt(0.77e2) * t166;
t297 = t120 * t307;
t296 = 0.2e1 * t109 + t346 + t339;
t295 = -0.2e1 * t111 + t342 + 0.4e1 * t158;
t294 = t111 + t343 + t339;
t293 = t111 + t120 - 0.2e1 * t158;
t119 = sin(phi);
t106 = t119 ^ 2;
t141 = sqrt(0.6e1);
t292 = -t106 * t141 / 0.4e1;
t291 = -0.6e1 * t111 + t344 - 0.20e2 * t158;
t290 = t111 + t341 + 0.10e2 * t158;
t288 = sqrt(0.273e3) / 0.64e2;
t287 = sqrt(0.33e2) / 0.64e2;
t137 = sqrt(0.13e2);
t286 = t137 / 0.64e2;
t144 = sqrt(0.2e1);
t285 = t144 / 0.32e2;
t284 = t144 / 0.64e2;
t283 = t61 / 0.128e3;
t282 = t348 + 0.18e2 * t111 - 0.18e2 * t158;
t281 = 0.18e2 * t109 - 0.38e2 * t111 + t342;
t135 = sqrt(0.15e2);
t280 = t135 / 0.128e3;
t279 = t144 / 0.128e3;
t278 = -0.1e1 - 0.9e1 * t114 + t337 + 0.5e1 * t161;
t277 = -0.5e1 * t114 + t337 + t318;
t276 = 0.7e1 * t159 - 0.3e1 * t161 - t66;
t275 = -t114 - t159 + t316;
t274 = 0.6e1 * t161 + 0.5e1 * t163 + t314;
t168 = t154 * t84;
t273 = (i) * t120 * t165 * t168;
t272 = -0.5e1 + 0.60e2 * t159 - 0.38e2 * t161 + t336;
t271 = -0.3e1 - 0.35e2 * t114 + 0.63e2 * t161 + t335;
t270 = -0.1e1 + t163 - 0.14e2 * t114 + 0.14e2 * t161;
t269 = t329 + 0.15e2 * t159 + t316;
t268 = -t106 * sqrt(0.10e2) * (t85 - 0.1e1) / 0.8e1;
t266 = 0.2e1 - 0.16e2 * t114 + 0.26e2 * t159 - 0.12e2 * t161;
t265 = 0.6e1 + 0.48e2 * t114 - 0.50e2 * t159 - 0.36e2 * t161;
t264 = -t109 - 0.9e1 * t111 + t341 + 0.5e1 * t158;
t57 = 0.1e1 / t153;
t263 = t57 * t283;
t262 = t347 - 0.11e2 * t111 + t305;
t155 = t106 ^ 2;
t104 = t106 * t155;
t124 = sqrt(0.231e3);
t261 = t104 * t124 / 0.32e2;
t260 = sqrt(0.70e2) * t155 / 0.16e2;
t259 = t153 * t283;
t258 = -0.15e2 * t109 + 0.21e2 * t111 - t120 - 0.5e1 * t158;
t257 = -0.7e1 * t109 - 0.19e2 * t111 - 0.9e1 * t120 + 0.35e2 * t158;
t256 = t348 + t332 + t340 + 0.14e2 * t158;
t255 = -t109 + t333 - 0.7e1 * t120 - 0.35e2 * t158;
t118 = sqrt(0.1430e4);
t254 = 0.3e1 / 0.256e3 * t155 ^ 2 * t118;
t126 = sqrt(0.143e3);
t253 = t126 * t279;
t130 = sqrt(0.55e2);
t252 = 0.3e1 / 0.128e3 * t130 * t144;
t132 = sqrt(0.35e2);
t251 = t132 * t165 * t304;
t250 = 0.16e2 - 0.210e3 * t159 + 0.196e3 * t161 + 0.30e2 * t163;
t249 = 0.12e2 * t107 - 0.14e2 * t109 + t332 + t344;
t248 = -0.17e2 * t109 + 0.7e1 * t111 - 0.11e2 * t120 + t327;
t247 = t347 + 0.69e2 * t111 - 0.29e2 * t120 - 0.15e2 * t158;
t246 = t334 - 0.66e2 * t109 + 0.78e2 * t111 + t328;
t245 = -0.25e2 * t109 - 0.77e2 * t111 + 0.17e2 * t120 + t327;
t244 = 0.30e2 * t109 - 0.10e2 * t111 + 0.18e2 * t120 + t328;
t243 = 0.715e3 * t161 - 0.1001e4 * t159 + 0.385e3 * t114 - 0.35e2;
t242 = t290 + t319;
t241 = t290 - t319;
t240 = -0.135e3 * t109 + t333 - 0.51e2 * t120 + 0.175e3 * t158;
t239 = 0.3e1 + t81 + t324 + 0.2e1 * t161 + t336;
t238 = 0.3e1 + t85 - 0.35e2 * t159 + 0.21e2 * t161 + t335;
t237 = (i) * t263;
t236 = 0.3e1 / 0.64e2 * (0.143e3 * t161 - 0.143e3 * t159 + 0.33e2 * t114 - 0.1e1) * t106 * t132;
t235 = 0.24e2 * t159 - 0.22e2 * t161 + 0.7e1 * t163 - t314;
t234 = t57 * t308 / 128;
t122 = sqrt(0.429e3);
t233 = t104 * t122 * (t329 - 0.1e1) / 0.64e2;
t127 = sqrt(0.105e3);
t79 = 0.33e2 * t159;
t232 = t106 * t127 * (t79 + t353) / 0.32e2;
t231 = t122 * t263;
t230 = t126 * t263;
t80 = 0.11e2 * t114;
t229 = 0.3e1 / 0.32e2 * sqrt(0.14e2) * t155 * (t80 - 0.1e1);
t228 = t137 * t263;
t227 = -0.1e1 + 0.14e2 * t114 - 0.52e2 * t159 + 0.66e2 * t161 - 0.27e2 * t163;
t225 = 0.7e1 - 0.42e2 * t114 + t324 + 0.90e2 * t161 - 0.75e2 * t163;
t224 = t120 * sqrt(0.42e2) * t153 / 0.16e2;
t223 = t144 * t153 * t289;
t82 = -0.26e2 * t114;
t222 = 0.3e1 / 0.128e3 * sqrt(0.154e3) * t155 * (0.65e2 * t159 + t82 + 0.1e1);
t221 = sqrt(0.15015e5) * t120 * t279;
t220 = (-0.1e1 / 0.2e1*i) * t141 * t297;
t219 = t294 + t302;
t218 = t293 + t303;
t217 = t293 - t303;
t216 = t294 - t302;
t215 = t277 + t306;
t214 = t277 - t306;
t213 = t334 + 0.62e2 * t109 - 0.162e3 * t111 - 0.10e2 * t120 + 0.90e2 * t158;
t212 = (-1*i) * t231;
t211 = (i) * t118 * t83 * t349;
t210 = sqrt(0.455e3) * t237;
t209 = (i) * t231;
t208 = sqrt(0.21e2) * t237;
t207 = (0.3e1 / 0.32e2) * sqrt(0.11e2) * t299;
t206 = t284 * t299;
t205 = t276 + t296;
t204 = -t276 + t296;
t203 = t275 + t295;
t202 = t275 - t295;
t201 = t257 + t300;
t200 = -t257 + t300;
t199 = t269 + t291;
t198 = t269 - t291;
t197 = t130 * t206;
t196 = sqrt(0.3e1) * t206;
t169 = t84 * t168;
t195 = (-1*i) * sqrt(0.2002e4) * t169 * t66 * t349;
t194 = sqrt(0.2310e4) * (0.39e2 * t159 + t82 + 0.3e1) * t273 / 64;
t193 = t127 * (t80 - 0.3e1) * t273 / 16;
t192 = t258 + t274;
t191 = -t258 + t274;
t190 = t262 + t266;
t189 = t262 - t266;
t188 = t239 + t281;
t187 = t256 + t270;
t186 = -t256 + t270;
t185 = -t239 + t281;
t184 = -t235 + t282;
t183 = t235 + t282;
t182 = t247 + t265;
t181 = t247 - t265;
t180 = t244 + t272;
t179 = t244 - t272;
t178 = t240 + t250;
t177 = -t240 + t250;
t176 = t227 + t249;
t175 = -t227 + t249;
t174 = -t226 + t246;
t173 = t226 + t246;
t172 = t213 + t225;
t171 = t213 - t225;
t151 = 4 * phi1;
t149 = 7 * phi1;
t142 = sqrt(0.5e1);
t140 = sqrt(0.7e1);
t101 = phi1 + t147;
t99 = phi1 - phi2;
t98 = phi1 + phi2;
t96 = phi1 + t146;
t92 = t151 + t147;
t91 = t151 + t146;
t88 = t149 + t148;
t87 = t149 + t145;
t86 = cos(t145);
t78 = exp((-6*i) * phi1);
t77 = exp((-5*i) * phi1);
t76 = exp((-4*i) * phi1);
t75 = exp((-3*i) * phi1);
t74 = exp((-2*i) * phi1);
t71 = exp((2*i) * phi1);
t70 = exp((3*i) * phi1);
t69 = exp((4*i) * phi1);
t68 = exp((5*i) * phi1);
t67 = exp((6*i) * phi1);
t52 = exp((-6*i) * t99);
t51 = exp((-6*i) * t98);
t48 = exp((-2*i) * t101);
t47 = exp((-2*i) * t96);
t42 = exp((-1*i) * t102);
t41 = exp((-1*i) * t95);
t38 = exp((-1*i) * t88);
t37 = exp((-1*i) * t87);
t32 = exp((i) * t88);
t31 = exp((i) * t87);
t30 = exp((2*i) * t101);
t29 = exp((2*i) * t96);
t22 = exp((6*i) * t99);
t21 = exp((6*i) * t98);
t7 = t38 * t323;
t6 = t31 * t323;

out_tvalues(1, :) = 1;
out_tvalues(2, :) = t74 * t292;
out_tvalues(3, :) = t73 * t220;
out_tvalues(4, :) = 0.3e1 / 0.2e1 * t114 - 0.1e1 / 0.2e1;
out_tvalues(5, :) = t72 * t220;
out_tvalues(6, :) = t71 * t292;
out_tvalues(7, :) = t76 * t260;
out_tvalues(8, :) = (t114 + t342 + 1) * t75 * t61 * t251;
out_tvalues(9, :) = t74 * t268;
out_tvalues(10, :) = t142 * t153 * (7 * t158 - 7 * t114 + t343 + 3) * t304 * t352;
out_tvalues(11, :) = 0.35e2 / 0.8e1 * t159 - 0.15e2 / 0.4e1 * t114 + 0.3e1 / 0.8e1;
out_tvalues(12, :) = (-0.1e1 / 0.4e1*i) * t72 * t142 * (t85 - 3) * t297;
out_tvalues(13, :) = t71 * t268;
out_tvalues(14, :) = t70 * t168 * t251;
out_tvalues(15, :) = t69 * t260;
out_tvalues(16, :) = -t78 * t261;
out_tvalues(17, :) = (t198 * t51 + t199 * t52) * t279;
out_tvalues(18, :) = (0.3e1 / 0.16e2*i) * (-3 * t114 - 1 + t305) * t77 * t61 * t298;
out_tvalues(19, :) = (t241 * t39 + t242 * t40 + t310) * t196;
out_tvalues(20, :) = t76 * t229;
out_tvalues(21, :) = (t214 * t45 + t215 * t46) * t287;
out_tvalues(22, :) = t75 * t193;
out_tvalues(23, :) = (t216 * t49 + t219 * t50) * t197;
out_tvalues(24, :) = -t74 * t232;
out_tvalues(25, :) = (t202 * t47 + t203 * t48) * t252;
out_tvalues(26, :) = (33 * t111 - 33 * t159 - 30 * t158 + t341 - t313) * t224 * t350;
out_tvalues(27, :) = (t217 * t41 + t218 * t42) * t207;
out_tvalues(28, :) = 0.231e3 / 0.16e2 * t161 - 0.315e3 / 0.16e2 * t159 + 0.105e3 / 0.16e2 * t114 - 0.5e1 / 0.16e2;
out_tvalues(29, :) = t124 * t86 * (t338 + 3 * t114 + t318) * t285;
out_tvalues(30, :) = (t79 + t313) * t224 * t351;
out_tvalues(31, :) = (t217 * t35 + t218 * t36) * t207;
out_tvalues(32, :) = -t71 * t232;
out_tvalues(33, :) = (t202 * t29 + t203 * t30) * t252;
out_tvalues(34, :) = t70 * t193;
out_tvalues(35, :) = (t216 * t23 + t219 * t24) * t197;
out_tvalues(36, :) = t69 * t229;
out_tvalues(37, :) = (t214 * t27 + t215 * t28) * t287;
out_tvalues(38, :) = (-0.3e1 / 0.16e2*i) * t68 * t169 * t298;
out_tvalues(39, :) = (t241 * t33 + t242 * t34 + t311) * t196;
out_tvalues(40, :) = -t67 * t261;
out_tvalues(41, :) = (t198 * t21 + t199 * t22) * t279;
out_tvalues(42, :) = (-1*i) * t140 * (t7 + (t255 + t301) * t38 + (-t264 + t278) * t37) * t259;
out_tvalues(43, :) = -(t181 * t51 - t182 * t52) * t279;
out_tvalues(44, :) = (-1*i) * (t179 * t39 + t180 * t40 + t310) * t228;
out_tvalues(45, :) = -(t200 * t45 + t201 * t46 + t321) * t286;
out_tvalues(46, :) = (-1*i) * (t185 * t49 + t188 * t50 + t312) * t230;
out_tvalues(47, :) = -(t189 * t47 - t190 * t48) * t253;
out_tvalues(48, :) = ((t344 - t183) * t42 + (t344 - t184) * t41) * t212;
out_tvalues(49, :) = (-1*i) * sqrt(0.3003e4) * t120 * sin(t145) * t104 * t285;
out_tvalues(50, :) = (t183 * t36 + t184 * t35 + t309) * t212;
out_tvalues(51, :) = -(-t189 * t29 + t190 * t30) * t253;
out_tvalues(52, :) = (i) * (t185 * t23 + t188 * t24 + t320) * t230;
out_tvalues(53, :) = (t200 * t27 + t201 * t28 + t322) * t286;
out_tvalues(54, :) = (i) * (t179 * t33 + t180 * t34 + t311) * t228;
out_tvalues(55, :) = -(-t181 * t21 + t182 * t22) * t279;
out_tvalues(56, :) = t140 * (t6 + (-t255 + t301) * t31 + (t264 + t278) * t32) * t234;
out_tvalues(57, :) = exp((-8*i) * phi1) * t254;
out_tvalues(58, :) = (t187 * exp((-2*i) * t92) + t186 * exp((-2*i) * t91)) * t280;
out_tvalues(59, :) = (-4 * t158 + 6 * t114 - 4 * t120 + t317) * exp((-7*i) * phi1) * t61 * t211;
out_tvalues(60, :) = (i) * t135 * (t7 + (t245 + t271) * t38 + (t238 - t248) * t37) * t259;
out_tvalues(61, :) = -t78 * t233;
out_tvalues(62, :) = (t177 * t51 + t178 * t52) * t279;
out_tvalues(63, :) = t77 * t195;
out_tvalues(64, :) = (t171 * t39 + t172 * t40) * t208;
out_tvalues(65, :) = t76 * t222;
out_tvalues(66, :) = (t191 * t45 + t192 * t46 + t321) * t288;
out_tvalues(67, :) = t75 * t194;
out_tvalues(68, :) = (t175 * t49 + t176 * t50 + t312) * t210;
out_tvalues(69, :) = -t74 * t236;
out_tvalues(70, :) = (t204 * t47 + t205 * t48) * t221;
out_tvalues(71, :) = (715 * t109 - 1001 * t111 + 385 * t158 - 35 * t120 - t243) * t223 * t350;
out_tvalues(72, :) = ((t340 + t174) * t42 + (t340 + t173) * t41) * t209;
out_tvalues(73, :) = 0.6435e4 / 0.128e3 * t163 - 0.3003e4 / 0.32e2 * t161 + 0.3465e4 / 0.64e2 * t159 - 0.315e3 / 0.32e2 * t114 + 0.35e2 / 0.128e3;
out_tvalues(74, :) = t122 * t226 * t86 * t284;
out_tvalues(75, :) = t243 * t223 * t351;
out_tvalues(76, :) = (t173 * t35 + t174 * t36 + t309) * t209;
out_tvalues(77, :) = -t71 * t236;
out_tvalues(78, :) = (t204 * t29 + t205 * t30) * t221;
out_tvalues(79, :) = t70 * t194;
out_tvalues(80, :) = (t175 * t23 + t176 * t24 + t320) * t210;
out_tvalues(81, :) = t69 * t222;
out_tvalues(82, :) = (t191 * t27 + t192 * t28 + t322) * t288;
out_tvalues(83, :) = t68 * t195;
out_tvalues(84, :) = (t171 * t33 + t172 * t34) * t208;
out_tvalues(85, :) = -t67 * t233;
out_tvalues(86, :) = (t177 * t21 + t178 * t22) * t279;
out_tvalues(87, :) = exp((7*i) * phi1) * t84 * t169 * t211;
out_tvalues(88, :) = t135 * (t6 + (-t245 + t271) * t31 + (t238 + t248) * t32) * t234;
out_tvalues(89, :) = exp((8*i) * phi1) * t254;
out_tvalues(90, :) = (t187 * exp((2*i) * t92) + t186 * exp((2*i) * t91)) * t280;
